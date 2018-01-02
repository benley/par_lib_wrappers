"""Helpers for zipped python binaries and Bazel runfiles"""

import atexit
import importlib
import logging as log
import os
import re
import shutil
import sys
import tempfile
import zipfile


def import_zipsafe(module_name):
    """Make it possible to import non-zipsafe modules from inside a zip.

    This is pretty weird and hopefully temporary.
    """
    module = importlib.import_module(module_name)
    zip_path = get_zip_path(module.__file__)
    if not zip_path:
        # It's not in a zip to begin with, so we're done.
        return module

    outdir = tempfile.mkdtemp()
    atexit.register(lambda: shutil.rmtree(outdir, ignore_errors=True))

    # module.__file__ is something like:
    #   "/home/foo/bar.par/something/module_name/__init__.py"
    # so relative_root will be:
    #   "something/module_name"
    relative_root = os.path.dirname(module.__file__)[len(zip_path)+1:]
    zf = BetterZipFile(zip_path)

    # Extract the zipped subtree under relative_root:
    for fn in zf.namelist():
        if fn.startswith(relative_root):
            zf.extract(member=fn, path=outdir)

    # Put the new importable location at the start of sys.path:
    if os.path.basename(module.__file__) == '__init__.py':
        new_path = os.path.dirname(os.path.join(outdir, relative_root))
    else:
        new_path = os.path.join(outdir, relative_root)
    touch(os.path.join(new_path, '__init__.py'))
    sys.path.insert(0, new_path)

    # Do our best to purge the module before trying to re-import it
    del module
    del(sys.modules[module_name])
    module = importlib.import_module(module_name)
    log.debug("extracted module: %s", module.__file__)
    return module


def get_zip_path(path):
    """If path is inside a zip file, return the zip file's path."""
    if path == os.path.sep:
        return None
    elif zipfile.is_zipfile(path):
        return path
    else:
        return get_zip_path(os.path.dirname(path))


def touch(fname, times=None):
    """Touch a file, like the unix touch command."""
    with open(fname, 'a'):
        os.utime(fname, times)


def find_runfiles():
    """Find the runfiles tree (useful when _not_ run from a zip file)"""
    # Follow symlinks, looking for my module space
    stub_filename = os.path.abspath(sys.argv[0])
    while True:
        # Found it?
        module_space = stub_filename + '.runfiles'
        if os.path.isdir(module_space):
            break

        runfiles_pattern = r"(.*\.runfiles)"
        matchobj = re.match(runfiles_pattern, os.path.abspath(sys.argv[0]))
        if matchobj:
            module_space = matchobj.group(1)
            break

        raise RuntimeError('Cannot find .runfiles directory for %s' %
                           sys.argv[0])
    log.debug("Found runfiles: %s", module_space)
    return module_space


def get_resource_filename(path):
    zip_path = get_zip_path(sys.modules.get("__main__").__file__)
    if zip_path:
        tmpdir = tempfile.mkdtemp()
        atexit.register(lambda: shutil.rmtree(tmpdir, ignore_errors=True))
        zf = BetterZipFile(zip_path)
        zf.extract(member=path, path=tmpdir)
        return os.path.join(tmpdir, path)
    elif os.path.exists(path):
        return path
    else:
        path_in_runfiles = os.path.join(find_runfiles(), path)
        if os.path.exists(path_in_runfiles):
            return path_in_runfiles
        else:
            raise ResourceNotFoundError


# FIXME(benley): This needs tests.
# It also may have some security implications pertaining to relative paths.
def get_resource_directory(path):
    """Find or extract an entire subtree and return its location."""
    zip_path = get_zip_path(sys.modules.get("__main__").__file__)
    if zip_path:
        tmpdir = tempfile.mkdtemp()
        atexit.register(lambda: shutil.rmtree(tmpdir, ignore_errors=True))
        zf = BetterZipFile(zip_path)
        members = []
        for fn in zf.namelist():
            if fn.startswith(path):
                members += [fn]
        zf.extractall(members=members, path=tmpdir)
        return os.path.join(tmpdir, path)
    elif os.path.exists(path):
        return path
    else:
        path_in_runfiles = os.path.join(find_runfiles(), path)
        if os.path.exists(path_in_runfiles):
            return path_in_runfiles
        else:
            raise ResourceNotFoundError


class ResourceNotFoundError(RuntimeError):
    pass


class BetterZipFile(zipfile.ZipFile):
    """Shim around ZipFile that preserves permissions on extract."""

    def extract(self, member, path=None, pwd=None):

        if not isinstance(member, zipfile.ZipInfo):
            member = self.getinfo(member)

        if path is None:
            path = os.getcwd()

        ret_val = self._extract_member(member, path, pwd)
        attr = member.external_attr >> 16
        os.chmod(ret_val, attr)
        return ret_val

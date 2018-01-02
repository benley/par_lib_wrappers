#!/usr/bin/env python
"""This is woefully incomplete"""

import os
import unittest
import tempfile

from par_lib_wrappers import resources


class TouchTests(unittest.TestCase):

    def setUp(self):
        self.tmp1 = tempfile.mktemp()
        self.tmp2 = tempfile.mktemp()

    def test_touch_creates_file(self):
        """touch creates files that don't exist"""
        tmpf = self.tmp1
        self.assertFalse(os.path.exists(tmpf))
        resources.touch(tmpf)
        self.assertTrue(os.path.exists(tmpf))

    def test_touch_sets_times(self):
        atime, mtime = 123, 456
        tmpf = self.tmp2
        resources.touch(tmpf, (atime, mtime))
        stat = os.stat(tmpf)
        self.assertEqual(stat.st_atime, atime)
        self.assertEqual(stat.st_mtime, mtime)

    def tearDown(self):
        try:
            os.unlink(self.tmp1)
            os.unlink(self.tmp2)
        except OSError:
            # they probably got cleaned up already
            pass


class ResourceTests(unittest.TestCase):

    def test_resource_extraction(self):
        """Dig up a source file as a resource and make sure it exists"""
        fp = resources.get_resource_filename(
            "par_lib_wrappers/par_lib_wrappers/resources.py")
        self.assertTrue(os.path.exists(fp))

    def test_extract_directory(self):
        """Dig up the directory containing a resource, make sure it exists"""
        path = resources.get_resource_directory(
            "par_lib_wrappers/par_lib_wrappers")
        self.assertTrue(os.path.exists(os.path.join(path, "resources.py")))


if __name__ == '__main__':
    unittest.main()

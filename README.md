# par_lib_wrappers

These are some examples of how to make shim libraries around Python
modules that are not zip-safe work inside .par or other zipped
archive without having to unpack the entire archive, and without
having to painstakingly fix the third-party modules directly.

The respository is set up for use with Bazel, since I figure if you're
using .par there's a good chance you're using Bazel too.

File an issue to let me know if you would find this more useful with a
setup.py, or with the WORKSPACE dependencies moved into an importable
.bzl file, or whatever else.

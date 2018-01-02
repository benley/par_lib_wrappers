"""botocore wrapper: makes botocore zip-safe for use in .par binaries"""

from par_lib_wrappers import resources

resources.import_zipsafe("botocore")
del resources

from python_botocore.botocore import *

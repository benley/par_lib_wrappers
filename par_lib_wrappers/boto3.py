"""boto3 wrapper: makes boto3 zip-safe for use in .par binaries"""

from par_lib_wrappers import resources

resources.import_zipsafe("botocore")
del resources

from python_boto3.boto3 import *  # noqa: E402, E403

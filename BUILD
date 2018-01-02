load("@subpar//:subpar.bzl", "par_binary")

py_library(
    name = "boto3",
    srcs = ["par_lib_wrappers/boto3.py"],
    deps = [
        "@python_boto3//:boto3",
        ":resources",
    ],
    visibility = ["//visibility:public"],
)

py_library(
    name = "botocore",
    srcs = ["par_lib_wrappers/botocore.py"],
    deps = [
        "@python_botocore//:botocore",
        ":resources",
    ],
    visibility = ["//visibility:public"],
)

py_library(
    name = "resources",
    srcs = ["par_lib_wrappers/resources.py"],
    visibility = ["//visibility:public"],
)

py_test(
    name = "resources_test",
    srcs = ["par_lib_wrappers/resources_test.py"],
    deps = [":resources"],
)

# Same as :resources_test, but explicitly build and run it from a .par binary
# to test resource extraction in both scenarios. "sh_test" just means "run this
# executable" here.
sh_test(
    name = "resources_par_test",
    srcs = [":resources_test_bin.par"],
    size = "small",
)

par_binary(
    name = "resources_test_bin",
    srcs = ["par_lib_wrappers/resources_test.py"],
    deps = [":resources"],
    main = "par_lib_wrappers/resources_test.py",
    # This should be testonly but can't be right now due to a subpar quirk
    # testonly = 1,
)

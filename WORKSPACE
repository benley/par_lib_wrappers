workspace(name = "par_lib_wrappers")

http_archive(
    name = "subpar",
    url = "https://github.com/google/subpar/archive/1.0.0.tar.gz",
    strip_prefix = "subpar-1.0.0",
    sha256 = "3e300d4326dc3661fd36b473cc42f5a6b0c856edb36f4cce33514d5b4d37f6f3",
)

new_http_archive(
    name = "python_botocore",
    url = "https://pypi.python.org/packages/fe/60/3ef1ebf6217217740c7467657b70347068195635f0a1b11ef1c37bd90e12/botocore-1.5.71.tar.gz",
    strip_prefix = "botocore-1.5.71",
    sha256 = "d5f5e1f4ea8df0efd7fa597ed2e6f73c620ea8696b5ec90779c46baa2012efb9",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "botocore",
    srcs = glob(["botocore/**/*.py"]),
    data = glob([
        "botocore/data/**",
        "botocore/vendored/requests/*.pem",
    ]),
    deps = [
        "@python_jmespath//:jmespath",
        "@python_dateutil//:dateutil",
        "@python_docutils//:docutils",
    ],
    visibility = ["//visibility:public"],
)
""",
)

new_http_archive(
    name = "python_boto3",
    url = "https://pypi.python.org/packages/58/61/50d2e459049c5dbc963473a71fae928ac0e58ffe3fe7afd24c817ee210b9/boto3-1.4.4.tar.gz",
    strip_prefix = "boto3-1.4.4",
    sha256 = "518f724c4758e5a5bed114fbcbd1cf470a15306d416ff421a025b76f1d390939",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "boto3",
    srcs = glob(["boto3/**/*.py"]),
    data = glob(["boto3/data/**"]),
    deps = [
        "@python_botocore//:botocore",
        "@python_jmespath//:jmespath",
        "@python_s3transfer//:s3transfer",
    ],
    visibility = ["//visibility:public"],
)
""",
)

new_http_archive(
    name = "python_s3transfer",
    url = "https://pypi.python.org/packages/8b/13/517e8ec7c13f0bb002be33fbf53c4e3198c55bb03148827d72064426fe6e/s3transfer-0.1.10.tar.gz",
    strip_prefix = "s3transfer-0.1.10",
    sha256 = "ba1a9104939b7c0331dc4dd234d79afeed8b66edce77bbeeecd4f56de74a0fc1",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "s3transfer",
    srcs = glob(["s3transfer/*.py"]),
    deps = [
        "@python_botocore//:botocore",
        "@python_futures//:futures",
    ],
    visibility = ["//visibility:public"],
)
""",
)

new_http_archive(
    name = "python_jmespath",
    url = "https://pypi.python.org/packages/e5/21/795b7549397735e911b032f255cff5fb0de58f96da794274660bca4f58ef/jmespath-0.9.3.tar.gz",
    strip_prefix = "jmespath-0.9.3",
    sha256 = "6a81d4c9aa62caf061cb517b4d9ad1dd300374cd4706997aff9cd6aedd61fc64",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "jmespath",
    srcs = glob(["jmespath/*.py"]),
    visibility = ["//visibility:public"],
    imports = ["."],
)
""",
)

new_http_archive(
    name = "python_futures",
    url = "https://pypi.python.org/packages/cc/26/b61e3a4eb50653e8a7339d84eeaa46d1e93b92951978873c220ae64d0733/futures-3.1.1.tar.gz",
    strip_prefix = "futures-3.1.1",
    sha256 = "51ecb45f0add83c806c68e4b06106f90db260585b25ef2abfcda0bd95c0132fd",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "futures",
    srcs = glob(["concurrent/futures/*.py"]),
    visibility = ["//visibility:public"],
    imports = ["."],
)
""",
)

new_http_archive(
    name = "python_docutils",
    url = "https://pypi.python.org/packages/05/fd/d62c2944d9df894b07eaa7430decc4c80977e644922a85fbdec337d6af82/docutils-0.14rc1.tar.gz",
    strip_prefix = "docutils-0.14rc1",
    sha256 = "7ee93a6fbab0f46bdda4d94384de40a04bbbbb53dbd019ce0fbbbfed22f6589a",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "docutils",
    srcs = glob(["docutils/**/*.py"]),
    data = glob([
        "docutils/**/*.txt",
        "docutils/**/*.css",
        "docutils/**/*.tex",
        "docutils/**/*.odt",
    ]),
    visibility = ["//visibility:public"],
    imports = ["."],
)
""",
)

new_http_archive(
    name = "python_dateutil",
    url = "https://pypi.python.org/packages/51/fc/39a3fbde6864942e8bb24c93663734b74e281b984d1b8c4f95d64b0c21f6/python-dateutil-2.6.0.tar.gz",
    strip_prefix = "python-dateutil-2.6.0",
    sha256 = "62a2f8df3d66f878373fd0072eacf4ee52194ba302e00082828e0d263b0418d2",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "dateutil",
    srcs = glob([
        "dateutil/*.py",
        "dateutil/tz/*.py",
        "dateutil/zoneinfo/*.py",
    ]),
    data = ["dateutil/zoneinfo/dateutil-zoneinfo.tar.gz"],
    deps = ["@python_six//:six"],
    visibility = ["//visibility:public"],
    imports = ["."],
)
""",
)

new_http_archive(
    name = "python_six",
    url = "https://pypi.python.org/packages/b3/b2/238e2590826bfdd113244a40d9d3eb26918bd798fc187e2360a8367068db/six-1.10.0.tar.gz",
    strip_prefix = "six-1.10.0",
    sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a",
    build_file_content = """
licenses(["notice"])

py_library(
    name = "six",
    srcs = ["six.py"],
    visibility = ["//visibility:public"],
    imports = ["."],
)
""",
)

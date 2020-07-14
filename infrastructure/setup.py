import setuptools


with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="swift-lambda",
    version="0.0.1",

    description="AWS CDK Python Infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "swift-lambda"},
    packages=setuptools.find_packages(where="swift-lambda"),

    install_requires=[
        "aws-cdk.core==1.45.0",
        "aws-cdk.aws_lambda==1.45.0",
        "aws-cdk.aws_iam==1.45.0",
        "aws-cdk.aws_s3==1.45.0",
    ],

    python_requires=">=3.8",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

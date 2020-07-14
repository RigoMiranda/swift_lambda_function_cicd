# Swift AWS Lambda CICD ![Main Workflow](https://github.com/RigoMiranda/swift_lambda_function_cicd/workflows/Main%20Workflow/badge.svg)

Deploy Swift Lambda Function into AWS using CDK and GitHub Actions

# Infrastructure
For more information go to [./infrastructure](https://github.com/RigoMiranda/swift_lambda_function_cicd/tree/master/infrastructure)

# Swift Lambda Function
These are the resources used to create AWS Lambda functions using swift:
* [Swift AWS Lambda Runtime](https://github.com/swift-server/swift-aws-lambda-runtime) by [Tomer Doron]
* [Getting started with Swift on AWS Lambda](https://fabianfett.de/getting-started-with-swift-aws-lambda-runtime) by [Fabian Fett](https://twitter.com/fabianfett)

The Lambda code is in [./swift-aws-lambda-square-number](https://github.com/RigoMiranda/swift_lambda_function_cicd/tree/master/swift-aws-lambda-square-number)

# CI/CD (GitHub Actions)
To automate the deployment of the Lambda function we will be using `GitHub Actions`. The workflow code can be found in `.github/workflows/main_workflow.yml`, and it will be used to do the following task:
* Download [Swift Docker](https://hub.docker.com/r/swiftlang/swift/tags) Image
* Docker Build
* Build Swift
* Packaging Swift dependencies for the Lambda
* Install AWS CLI & Configuring Profile Credentials
* Installing AWS CDK and Dependencies
* Deploying the Lambda Function

### AWS Credential
The AWS credentials are stored as [GitHub Secrets](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets), and they can ba access using this code `${{ secrets.AWS_ACCESS_KEY_ID }}`

# TODO
* Add Cache for the Docker Image
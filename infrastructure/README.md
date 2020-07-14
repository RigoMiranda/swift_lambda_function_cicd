
# Swift Lambda Function Deployment With AWS CDK

This project uses [AWS CDK](https://aws.amazon.com/cdk/) (infrastructure as code) and `Python ^3.8` to create the infrastructure used to deploy the Swift lambda function.  

# Get Started
To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Notes:
* The `cdk.json` file tells the CDK Toolkit how to execute your app.
* To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

# Building the Infrastructure
In the file `swift_lambda/swift_lambda_stack.py` we are creating the class `SwiftLambdaCdkStack`. This class will represent a `CloudFormation Stack`. Using the code below, is how an `AWS Lambda` is defined on `AWS CDK`. 

It is very important to understand that currently, `Swift` is not a support language for AWS Lambdas, but AWS supports the use of [Custom AWS Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html). That is the reason why in the `runtime` we have the value of `aws_lambda.Runtime.PROVIDED`, because we will be providing our own custom Lambda runtime.

```python
aws_lambda.Function(
        scope         = self,
        id            = 'square_number_lambda_function',
        function_name = 'SquareNumber',
        code          = aws_lambda.Code.from_asset('../swift-aws-lambda-square-number/.build/lambda/SquareNumber'),
        handler       = 'SquareNumber.main',
        runtime       = aws_lambda.Runtime.PROVIDED,
        memory_size   = 512,
        timeout       = core.Duration.seconds(120)
    )
```

*Note: The Swift Lambda runtime will be created in `../swift-aws-lambda-square-number`*

In this case, `app.py` is the AWS CDK main file. In this file is were we will be importing the CloudFormation Stack that AWS CDK will be creating and deploying. In the code below, we are using the class `SwiftLambdaCdkStack` to create the CloudFormation that will deploy the Lambda function and we are giving is an `id` of `swift-lambda` (any name can be used) that will be used during the deployment.  

```python
# CloudFormation Stack:
lambda_stack = SwiftLambdaCdkStack(
    scope = app,
    id    = "swift-lambda",
    env   = env
)
```

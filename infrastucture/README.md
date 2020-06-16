
# Swift Lambda Function Deployment With AWS CDK

This project uses AWS CDK (infrastructure as code) and `Python ^3.8` to create the infrastructure used to deploy the Swift lambda function.  

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

# Swift Lambda Function
For information on how to create AWS Lambda functions using swift visit:
* [Swift AWS Lambda Runtime](https://github.com/swift-server/swift-aws-lambda-runtime) by [Tomer Doron]
* [Getting started with Swift on AWS Lambda](https://fabianfett.de/getting-started-with-swift-aws-lambda-runtime) by [Fabian Fett](https://twitter.com/fabianfett)

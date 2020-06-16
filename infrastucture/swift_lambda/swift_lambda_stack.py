from aws_cdk import core
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.aws_iam as iam

'''
    Documentation:
    — https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Function.html
'''

class SwiftLambdaCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = aws_lambda.Function(
            scope         = self,
            id            = 'square_number_lambda_function',
            function_name = 'SquareNumber',
            code          = aws_lambda.Code.from_asset('../swift-aws-lambda-square-number/.build/lambda/SquareNumber'),
            handler       = 'SquareNumber.main',
            runtime       = aws_lambda.Runtime.PROVIDED,
            memory_size   = 512,
            timeout       = core.Duration.seconds(120)
        )
#!/usr/bin/env python3

from aws_cdk import core

from swift_lambda.swift_lambda_stack import SwiftLambdaCdkStack

app = core.App()
env = {'region': 'us-east-1'}

# CloudFormation Stack:
lambda_stack = SwiftLambdaCdkStack(
    scope = app,
    id    = "swift-lambda",
    env   = env
)

# Adding Tags Resources:
tags = {
    'Environment': 'dev',
    'Name': 'Swift Lambda Functions',
    'Provisioner': 'AWS CDK'
    'Version' '0.0.1'
}

for tag, value in tags.items():
    core.Tag.add(lambda_stack, tag, value)


app.synth()

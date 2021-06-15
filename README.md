# Serverless / Lambda Deployment Exercise

This repository contains a serverless / lambda aws deployment utilizing terraforms for 
deployment automation. It consists of a caching gateway which calls a lambda function. The
lambda function writes a time stamp and a variable to a file contained within a s3 bucket. 

# Files

main.tf (terraforms application deployment)\
hello.py (lambda function)\

# Requires

Deployment requires the following
terraforms\
aws account\

**export your api id and secret and a region**\
export AWS_ACCESS_KEY_ID="xxxxxxx"\
export AWS_SECRET_ACCESS_KEY="xxxxxxx"\
export AWS_DEFAULT_REGION="us-east-1"\

## Deploy
Clone this repository and run the following in the root of the directory
terraforms init

Continue by running a plan
terraforms init

Finally you can deploy by running apply
terraforms apply


## AWS Components
s3 bucket (homeworkhellobucket)
lambda function (homework_labda)
aws api gateway with caching
cloudwatch log group (lambda_logging)

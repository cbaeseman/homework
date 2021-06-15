import json, boto3,os, sys, uuid
from urllib.parse import unquote_plus
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    if 'queryStringParameters' in event:
        thevar = event['queryStringParameters']['thevar']
    else:
        thevar = "default"

    if 'thevar' in event:
        thevar = event['thevar']

    bucket_name = "homeworkhellobucket"
    file_name = "hello-world.txt"
    lambda_path = "/tmp/" + file_name
    s3_path = "output/" + file_name

    open(lambda_path,"w+").write(str(datetime.now()) + ' ' + thevar)
    s3 = boto3.resource("s3")
    s3.meta.client.upload_file(lambda_path, bucket_name, file_name)

    return {
        'statusCode': 200,
        'body': json.dumps('file is created in:' + s3_path + ':' + thevar)
    }


# https://aws-lambda-for-python-developers.readthedocs.io/en/latest/02_event_and_context/
# https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
# https://www.youtube.com/watch?v=Lkm3v7UDlD8
# https://www.youtube.com/watch?v=wf5kLfSM9C0&list=PLH1ul2iNXl7vk8RUchIiMBeXqDnFTi4_M&index=5
import boto3
import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

hostname = os.environ.get("LOCALSTACK_HOSTNAME")
endpoint_url = f'http://{hostname}:4566'
dynamodb = boto3.resource('dynamodb', endpoint_url = endpoint_url)
table = dynamodb.Table('users')

def lambda_handler(event, context):
    eventBody = event['Records'][0]['body'] # eventBody is a string
    json_body = json.loads(eventBody)

    user = {}
    user['username'] = json_body['FirstName']
    user['last_name'] = json_body['LastName']

    logger.info('Before creating item in DynamoDB')
    # the Item argument expects a dictionary object
    response = table.put_item(
        Item = user
    )
    
    logger.info('Item created in DynamoDB')

    
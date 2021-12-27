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

    
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-examples.html

import boto3
import random
import string
import json

endpoint_url = "http://localhost:4566"
#endpoint_url = "https://queue.amazonaws.com"

queue_url = "http://localhost:4566/000000000000/lambda"
# Create SQS client
sqs = boto3.client('sqs', endpoint_url=endpoint_url)


def generateRandomString():
    random_string = string.ascii_lowercase
    return ''.join(random.choice(random_string) for i in range(10))

data = {}
data['FirstName'] = generateRandomString()
data['LastName'] = generateRandomString()

json_data = json.dumps(data)

#Send message to SQS queue
response = sqs.send_message(
    QueueUrl= queue_url,
    DelaySeconds=5,
    MessageBody=(
        json_data
    )
)

print(response['MessageId'])

# awsl sqs list-queues
# awsl sqs receive-message --queue-url http://localhost:4566/000000000000/lambda
# awsl sqs purge-queue --queue-url http://localhost:4566/000000000000/lambda
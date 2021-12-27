# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-examples.html

import boto3

endpoint_url = "http://localhost:4566"
#endpoint_url = "https://queue.amazonaws.com"

queue_url = "http://localhost:4566/000000000000/test"
# Create SQS client
sqs = boto3.client('sqs', endpoint_url=endpoint_url)

response = sqs.receive_message(
    QueueUrl= queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)

# AWS CLI examples
# awsl sqs receive-message --queue-url http://localhost:4566/000000000000/test
# awsl sqs purge-queue --queue-url http://localhost:4566/000000000000/test
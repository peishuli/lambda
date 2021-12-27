import boto3
endpoint_url = "http://localhost:4566"

dynamodb = boto3.resource('dynamodb', endpoint_url = endpoint_url)
table = dynamodb.Table('users')
#print(table.creation_date_time)
table.put_item(
    Item={
        'username': 'johnsmith',
        'last_name': 'Smith'
    }
)

# awsl dynamodb list-tables
# awsl dynamodb scan --table-name users
# awsl dynamodb scan --table-name users | jq '.Count'
# awsl dynamodb get-item --table-name users --key '{"username": {"S": "joedoe"}, {"last_name": {"S": "Doe"}}'
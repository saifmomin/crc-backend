import json
import boto3
import os

print('Loading function')

# Create the DynamoDB Client outside handler
region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']


def lambda_handler(event, context):
    # Create the DynamoDB Table Resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Use Atomic Counter to increment website visit count
    response = table.update_item(Key={"website": "saifmomin.net"},
                                 UpdateExpression='SET visits = visits + :increment',
                                 ExpressionAttributeValues={':increment': 1},
                                 ReturnValues="UPDATED_NEW"
                                 )

    # Use the DynamoDB Table resource get item method to get a single item
    response = table.get_item(Key={'website': 'saifmomin.net'}
                              )

    count = response['Item']['visits']

    # Return format as expected by API Gateway
    return {
        "statusCode": 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        "body": count
    }

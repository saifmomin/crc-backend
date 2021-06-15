import json
import boto3
import os

print('Loading function')

# Creating the DynamoDB Client
region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']


def lambda_handler(event, context):
    # Creating the DynamoDB Table Resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)


    response = table.update_item(Key={"visitor": "guest"},
                                 UpdateExpression='SET counts = counts + :increment',
                                 ExpressionAttributeValues={':increment': 1},
                                 ReturnValues="UPDATED_NEW"
                                 )

    # Use the DynamoDB Table resource get item method to get a single item
    response = table.get_item(Key={'visitor': 'guest'}
                              )

    count = response['Item']['counts']
    print(count)
    # return count

    return {
        #"statusCode": 200,
        #"headers": {},
        #"body": json.dumps(decimal.Decimal(count), default=decimal_default)
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        "body": count
    }

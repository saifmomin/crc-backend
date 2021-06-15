'''
Created on 08-Jun-2021

@author: saif
'''
from pprint import pprint
import boto3


def create_visitor_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

    table = dynamodb.create_table(
        TableName='Visitors',
        KeySchema=[
            {
                'AttributeName': 'visitor',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'visitor',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='Visitors')
    assert table.table_status == 'ACTIVE'

    return table


if __name__ == '__main__':
    visitor_table = create_visitor_table()
    print("Table status:", visitor_table.table_status)


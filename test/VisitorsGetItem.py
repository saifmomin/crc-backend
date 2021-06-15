'''
Created on 08-Jun-2021

@author: saif
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_visitor(visitor, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')

    try:
        response = table.get_item(Key={'visitor': 'guest'})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    visitor = get_visitor("guest")
    if visitor:
        print("Get visitor succeeded:")
        pprint(visitor, sort_dicts=False)
'''
Created on 08-Jun-2021

@author: saif
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def update_visitor(website, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')
    response = table.update_item(
                                Key={ "website":"saifmomin.net"},
                                UpdateExpression='SET visits = visits + :increment',
                                ExpressionAttributeValues={':increment': 1},
                                ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    visitor_resp = update_visitor("saifmomin.net")
    print("Update visitor succeeded:")
    pprint(visitor_resp, sort_dicts=False)
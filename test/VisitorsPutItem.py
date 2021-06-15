'''
Created on 08-Jun-2021

@author: saif
'''
from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def put_visitor(visitor, counts, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Visitors')
    response = table.put_item(
       Item={
                'visitor': visitor,
                'counts': counts,
            }
    )
    return response

if __name__ == '__main__':
    visitor_resp = put_visitor("guest", 1, 0)
    print("Put visitor succeeded:")
    pprint(visitor_resp, sort_dicts=False)
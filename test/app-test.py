'''
Created on 08-Jun-2021

@author: saif
'''
from pprint import pprint
import unittest

import boto3
from botocore.exceptions import ClientError

from moto import mock_dynamodb2


@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):

    def setUp(self):
        """Create the mock database and table"""
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        from VisitorsCreateTable import create_visitor_table
        self.table = create_visitor_table(self.dynamodb)

    def tearDown(self):
        """Delete mock database and table after test is run"""
        self.table.delete()
        self.dynamodb = None

    def test_table_exists(self):
        self.assertTrue(self.table)  # check if we got a result
        self.assertIn('Visitors', self.table.name)  # check if the table name is 'Movies'
        # pprint(self.table.name)

    def test_put_visitor(self):
        from VisitorsPutItem import put_visitor

        result = put_visitor("guest1", 1, self.dynamodb)

        self.assertEqual(200, result['ResponseMetadata']['HTTPStatusCode'])
        # pprint(result, sort_dicts=False)

    def test_get_visitor(self):
        from VisitorsPutItem import put_visitor
        from VisitorsGetItem import get_visitor

        put_visitor("guest", 1, self.dynamodb)
        result = get_visitor("guest", self.dynamodb)

        # self.assertEqual('guest', result[‘visitor’])
        # self.assertEqual(1, result[‘counts’])
        self.assertEqual("guest", get_visitor("guest", self.dynamodb)['visitor'])
        self.assertEqual(1, get_visitor("guest", self.dynamodb)['counts'])
        # pprint(result, sort_dicts=False)

    def test_update_visitor(self):
        from VisitorsPutItem import put_visitor
        from VisitorsGetItem import get_visitor
        from VisitorsUpdateItem import update_visitor

        put_visitor("guest", 2, self.dynamodb)
        result = update_visitor("guest", self.dynamodb)

        self.assertEqual("guest", get_visitor("guest", self.dynamodb)['visitor'])
        self.assertEqual(4, get_visitor("guest", self.dynamodb)['counts'])
        # pprint(result, sort_dicts=False)


if __name__ == '__main__':
    unittest.main()


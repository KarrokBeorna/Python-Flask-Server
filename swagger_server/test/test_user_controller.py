# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_order import CreateOrder  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_order(self):
        """Test case for create_order

        Create order
        """
        body = CreateOrder()
        response = self.client.open(
            '//order',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_history(self):
        """Test case for get_order_history

        Displaying order history
        """
        response = self.client.open(
            '//orderHistory',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_shops(self):
        """Test case for get_shops

        Get shops
        """
        response = self.client.open(
            '//getShops',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

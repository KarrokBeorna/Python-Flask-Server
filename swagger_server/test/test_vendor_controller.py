# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.add_shop import AddShop  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVendorController(BaseTestCase):
    """VendorController integration test stubs"""

    def test_add_product(self):
        """Test case for add_product

        Add product
        """
        query_string = [('product', 'product_example'),
                        ('price', 789)]
        response = self.client.open(
            '//product',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_shop(self):
        """Test case for add_shop

        Add shop
        """
        body = AddShop()
        response = self.client.open(
            '//shop',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_shop_history(self):
        """Test case for get_shop_history

        Displaying shop history
        """
        response = self.client.open(
            '//shopHistory',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

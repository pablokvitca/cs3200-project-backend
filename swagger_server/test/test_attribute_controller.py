# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.attribute import Attribute  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAttributeController(BaseTestCase):
    """AttributeController integration test stubs"""

    def test_add_attribute(self):
        """Test case for add_attribute

        Add a attribute to the classdeck
        """
        body = Attribute()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/attribute',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_attribute(self):
        """Test case for delete_attribute

        Deletes a attribute
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/attribute/{attribute_name}'.format(attribute_name='attribute_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_attribute_by_name(self):
        """Test case for get_attribute_by_name

        Find attribute by name
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/attribute/{attribute_name}'.format(attribute_name='attribute_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_attribute(self):
        """Test case for update_attribute

        Update an existing attribute
        """
        body = Attribute()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/attribute',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.class_attribute import ClassAttribute  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassAttributeController(BaseTestCase):
    """ClassAttributeController integration test stubs"""

    def test_add_class_attribute(self):
        """Test case for add_class_attribute

        Add a class_attribute to the classdeck
        """
        body = ClassAttribute()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_attribute',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_class_attribute(self):
        """Test case for delete_class_attribute

        Deletes a class_attribute
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_attribute/{attribute_name}/{class_department}/{class_number}'.format(attribute_name='attribute_name_example', class_department='class_department_example', class_number=9999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_class_attribute_by_id(self):
        """Test case for get_class_attribute_by_id

        Find class_attribute by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_attribute/{attribute_name}/{class_department}/{class_number}'.format(attribute_name='attribute_name_example', class_department='class_department_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_class_attribute(self):
        """Test case for update_class_attribute

        Update an existing class_attribute
        """
        body = ClassAttribute()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_attribute',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

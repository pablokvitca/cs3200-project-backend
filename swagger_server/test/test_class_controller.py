# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassController(BaseTestCase):
    """ClassController integration test stubs"""

    def test_add_class(self):
        """Test case for add_class

        Add a class to the classdeck
        """
        body = ModelClass()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class/filtered',
            method='GET',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_class_by_id(self):
        """Test case for get_class_by_id

        Find class by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class/{class_department}/{class_number}'.format(class_department='class_department_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_classes(self):
        """Test case for list_classes

        List all classes
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

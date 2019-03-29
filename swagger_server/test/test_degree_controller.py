# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.degree import Degree  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDegreeController(BaseTestCase):
    """DegreeController integration test stubs"""

    def test_add_degree(self):
        """Test case for add_degree

        Add a degree to the classdeck
        """
        body = Degree()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_degree(self):
        """Test case for delete_degree

        Deletes a degree
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree/{degree_id}'.format(degree_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_degree_by_id(self):
        """Test case for get_degree_by_id

        Find degree by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree/{degree_id}'.format(degree_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_degree(self):
        """Test case for update_degree

        Update an existing degree
        """
        body = Degree()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/degree',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

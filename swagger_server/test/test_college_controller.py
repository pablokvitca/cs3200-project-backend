# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.college import College  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCollegeController(BaseTestCase):
    """CollegeController integration test stubs"""

    def test_add_college(self):
        """Test case for add_college

        Add a college to the classdeck
        """
        body = College()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/college',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_college(self):
        """Test case for delete_college

        Deletes a college
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/college/{college_id}'.format(college_id=1),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_college_by_id(self):
        """Test case for get_college_by_id

        Find college by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/college/{college_id}'.format(college_id=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_college(self):
        """Test case for update_college

        Update an existing college
        """
        body = College()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/college',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

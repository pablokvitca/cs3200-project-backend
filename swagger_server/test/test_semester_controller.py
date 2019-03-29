# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.semester import Semester  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSemesterController(BaseTestCase):
    """SemesterController integration test stubs"""

    def test_add_semester(self):
        """Test case for add_semester

        Add a semester to the classdeck
        """
        body = Semester()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/semester',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_semester(self):
        """Test case for delete_semester

        Deletes a semester
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/semester/{semester}/{year}'.format(semester='semester_example', year=3000),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_semester_by_id(self):
        """Test case for get_semester_by_id

        Find semester by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/semester/{semester}/{year}'.format(semester='semester_example', year=3000),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_semester(self):
        """Test case for update_semester

        Update an existing semester
        """
        body = Semester()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/semester',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

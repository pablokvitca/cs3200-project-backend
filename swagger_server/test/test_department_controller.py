# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.department import Department  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDepartmentController(BaseTestCase):
    """DepartmentController integration test stubs"""

    def test_add_department(self):
        """Test case for add_department

        Add a department to the classdeck
        """
        body = Department()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/department',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_department(self):
        """Test case for delete_department

        Deletes a department
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/department/{department_short_code}'.format(department_short_code='department_short_code_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_department_by_short_code(self):
        """Test case for get_department_by_short_code

        Find department by short code
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/department/{department_short_code}'.format(department_short_code='department_short_code_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_department(self):
        """Test case for update_department

        Update an existing department
        """
        body = Department()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/department',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

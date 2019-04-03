# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.department import Department  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDepartmentController(BaseTestCase):
    """DepartmentController integration test stubs"""

    def test_get_department_by_short_code(self):
        """Test case for get_department_by_short_code

        Find department by short code
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/department/{department_short_code}'.format(department_short_code='department_short_code_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_department(self):
        """Test case for list_department

        List all departments
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/department',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

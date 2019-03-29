# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentController(BaseTestCase):
    """StudentController integration test stubs"""

    def test_create_student(self):
        """Test case for create_student

        Create student
        """
        body = Student()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_student(self):
        """Test case for delete_student

        Delete student
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student/{nuid}'.format(nuid='nuid_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_student_by_nuid(self):
        """Test case for get_student_by_nuid

        Get student by nuid
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student/{nuid}'.format(nuid=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_student(self):
        """Test case for login_student

        Logs student into the system
        """
        query_string = [('nuid', 'nuid_example'),
                        ('password', 'password_example')]
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student/login',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_student(self):
        """Test case for logout_student

        Logs out current logged in student session
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_student(self):
        """Test case for update_student

        Updated student
        """
        body = Student()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student/{nuid}'.format(nuid=2),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

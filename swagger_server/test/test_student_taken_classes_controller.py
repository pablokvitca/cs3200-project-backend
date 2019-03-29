# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.student_taken_classes import StudentTakenClasses  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentTakenClassesController(BaseTestCase):
    """StudentTakenClassesController integration test stubs"""

    def test_add_student_taken_classes(self):
        """Test case for add_student_taken_classes

        Add a student_taken_classes to the classdeck
        """
        body = StudentTakenClasses()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student_taken_classes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_student_taken_classes(self):
        """Test case for delete_student_taken_classes

        Deletes a student_taken_classes
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student_taken_classes/{nuid}/{class_dept}/{class_number}'.format(nuid=1, class_dept='class_dept_example', class_number=9999),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_student_taken_classes_by_id(self):
        """Test case for get_student_taken_classes_by_id

        Find student_taken_classes by ID
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student_taken_classes/{nuid}/{class_dept}/{class_number}'.format(nuid=2, class_dept='class_dept_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_student_taken_classes(self):
        """Test case for update_student_taken_classes

        Update an existing student_taken_classes
        """
        body = StudentTakenClasses()
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/student_taken_classes',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

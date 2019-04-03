# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestClassAttributeController(BaseTestCase):
    """ClassAttributeController integration test stubs"""

    def test_get_class_attributes(self):
        """Test case for get_class_attributes

        Lists attributes for the given class
        """
        response = self.client.open(
            '/pablokvitca/classdeck-api/1.0.0/class_attribute/{class_department}/{class_number}'.format(class_department='class_department_example', class_number=9999),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

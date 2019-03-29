import connexion
import six

from swagger_server.models.attribute import Attribute  # noqa: E501
from swagger_server import util

import sqlalchemy
from sqlalchemy import create_engine

def add_attribute(body):  # noqa: E501
    """Add a attribute to the classdeck

     # noqa: E501

    :param body: Attribute object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
        settings = {
            'userName': "root",           # The name of the MySQL account to use (or empty for anonymous)
            'password': "WRITE PASSWORD HERE",           # The password for the MySQL account (or empty for anonymous)
            'serverName': "127.0.0.1",    # The name of the computer running MySQL
            'portNumber': 3306,           # The port of the MySQL server (default is 3306)
            'dbName': "projectcs3200",             # The name of the database we are testing with (this default is installed with MySQL)
        }
        print('Trying to connect to database')
        conn = create_engine('mysql+mysqldb://{0[userName]}:{0[password]}@{0[serverName]}:{0[portNumber]}/{0[dbName]}'.format(settings))
        print('Connected to database')
        tableName = "attributes"
        insert_string = """
            INSERT INTO {} (
                name,
                nu_path)
            VALUES (
                "{}",
                {});
            """.format(tableName, body.name, body.nupath)
        print(insert_string)
        conn.execute(insert_string)
    return 'do some magic!'


def delete_attribute(attribute_name):  # noqa: E501
    """Deletes a attribute

     # noqa: E501

    :param attribute_name: name of the attribute to delete
    :type attribute_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_attribute_by_name(attribute_name):  # noqa: E501
    """Find attribute by name

    Returns a single attribute # noqa: E501

    :param attribute_name: name of attribute to return
    :type attribute_name: str

    :rtype: Attribute
    """
    return 'do some magic!'


def update_attribute(body):  # noqa: E501
    """Update an existing attribute

     # noqa: E501

    :param body: Attribute object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

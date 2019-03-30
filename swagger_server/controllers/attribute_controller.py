import connexion
import six

from swagger_server.models.attribute import Attribute  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc

def add_attribute(body):  # noqa: E501
    """Add a attribute to the classdeck

     # noqa: E501

    :param body: Attribute object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
        insert_string = """
            INSERT INTO attributes (
                name,
                nu_path)
            VALUES (
                "{}",
                {});
            """.format(body.name, body.nupath)
        try:
            connexion.DB.execute(insert_string)
            return "Accepted", 201
        except exc.IntegrityError:
            return "Already Exists", 202
    return "Bad Request", 400


def delete_attribute(attribute_name):  # noqa: E501
    """Deletes a attribute

     # noqa: E501

    :param attribute_name: name of the attribute to delete
    :type attribute_name: str

    :rtype: None
    """
    delete_string = """
        DELETE FROM attributes
        WHERE name = "{}"
        """.format(attribute_name)
    try:
        connexion.DB.execute(delete_string)
        return "Deleted", 204
    except exc.IntegrityError:
        return "Could not delete object", 403


def get_attribute_by_name(attribute_name):  # noqa: E501
    """Find attribute by name

    Returns a single attribute # noqa: E501

    :param attribute_name: name of attribute to return
    :type attribute_name: str

    :rtype: Attribute
    """
    select_string = """
        SELECT * FROM attributes
        WHERE name = "{}"
        """.format(attribute_name)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'name': row["name"],
                'nupath': row["nu_path"] 
            }
            res = Attribute.from_dict(res)
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def update_attribute(body):  # noqa: E501
    """Update an existing attribute

     # noqa: E501

    :param body: Attribute object that needs to be updated in the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Attribute.from_dict(connexion.request.get_json())  # noqa: E501
        update_string = """
            INSERT INTO attributes (
                name,
                nu_path)
            VALUES (
                "{0}",
                {1})
            ON DUPLICATE KEY 
            UPDATE
                name = "{0}", 
                nu_path = {1};
            """.format(body.name, body.nupath)
        try:
            connexion.DB.execute(update_string)
            return "Accepted", 201
        except exc.IntegrityError:
            return "Already Exists", 202
    return "Bad Request", 400

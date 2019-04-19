import connexion
import six

from swagger_server.models.attribute import Attribute  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc


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
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
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


def list_attributes():  # noqa: E501
    """List all attributes

    Returns all attributes # noqa: E501


    :rtype: None
    """
    select_string = """
                SELECT * FROM attributes
                """
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
        res = []
        for row in result:
            r = Attribute.from_dict(row)
            res.append({
                'name': row["name"],
                'nupath': row["nupath"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500

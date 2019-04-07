import connexion
import six

from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc


def get_class_by_id(class_department, class_number):  # noqa: E501
    """Find class by ID

    Returns a single class # noqa: E501

    :param class_department: short code of the department that offers the class to return
    :type class_department: str
    :param class_number: class number of the class to return
    :type class_number: int

    :rtype: ModelClass
    """
    select_string = """
                    SELECT * FROM class
                    WHERE class_dept = "{0}" AND class_number = "{1}"
                    """.format(class_department, class_number)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'class_level': row["class_level"],
                'name': row["name"],
                'description': row["description"],
                'credit_hours': row["credit_hours"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_classes():  # noqa: E501
    """List all classes

    Returns all classes # noqa: E501


    :rtype: None
    """
    select_string = """
            SELECT * FROM class
            """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for row in result:
            r = ModelClass.from_dict(row)
            res.append({
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'class_level': row["class_level"],
                'name': row["name"],
                'description': row["description"],
                'credit_hours': row["credit_hours"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_classes_filtered():  # noqa: E501
    """List all classes

    Returns all classes # noqa: E501


    :rtype: None
    """
    select_string = """
              SELECT * FROM class
              """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for row in result:
            res.append({
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'class_level': row["class_level"],
                'name': row["name"],
                'description': row["description"],
                'credit_hours': row["credit_hours"]
            })
            res = ModelClass.from_dict(res)
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500

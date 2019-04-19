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
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
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
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
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
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_classes_by_semester(semester):
    select_string = """
                SELECT
                    DISTINCT
                    c.class_dept,
                    c.class_number,
                    c.class_level,
                    c.name,
                    c.description,
                    c.credit_hours
                FROM class AS c
                RIGHT OUTER JOIN section AS s ON c.class_dept = s.class_dept AND c.class_number = s.class_number
                WHERE s.semester_id = {0};
                """.format(semester)
    try:
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
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
        if len(res) > 0:
            return res, 200
        else:
            return "No classes found", 404
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
        db_conn = connexion.DB(connexion.DB_ENG)
        result = db_conn.execute(select_string)
        db_conn.close()
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
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500

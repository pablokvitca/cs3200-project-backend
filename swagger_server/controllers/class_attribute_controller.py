import connexion
import six


from swagger_server.models.class_attribute import ClassAttribute  # noqa: E501
from swagger_server import util


from sqlalchemy import types
from sqlalchemy import exc

def get_class_attributes(class_department, class_number):  # noqa: E501
    """Lists attributes for the given class

    Returns a attributes for the given class # noqa: E501

    :param class_department: short code of the Department related to the Class related to the ClassAttribute to return
    :type class_department: str
    :param class_number: number of the Class related to the ClassAttribute to return
    :type class_number: int

    :rtype: None
    """

    select_string = """
                        SELECT * FROM class_attribute
                        WHERE class_dept = "{0}" AND class_number = "{1}"
                        """.format(class_department, class_number)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'attr_name': row["attr_name"],
                'class_dept': row["class_dept"],
                'class_number': row["class_number"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500

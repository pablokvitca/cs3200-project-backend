import connexion
import six

from swagger_server.models.section import Section  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc


def add_section():  # noqa: E501
    """Add a section to the classdeck

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_section_by_crn(crn):  # noqa: E501
    """Find section by

    Returns a single section # noqa: E501

    :param crn: CRN of section to return
    :type crn: int

    :rtype: Section
    """
    select_string = """
                        SELECT * FROM section
                        WHERE CRN = "{}"
                        """.format(crn)
    try:
        result = connexion.DB.execute(select_string)
        for row in result:
            res = {
                'CRN': row["CRN"],
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'professor': row["professor"],
                'capacity': row["capacity"],
                'registered': row["registered"]
            }
            return res, 200
        return "Object not found", 404
    except exc.IntegrityError:
        return "Internal Server Error", 500


def list_sections():  # noqa: E501
    """Lists all sections

     # noqa: E501


    :rtype: None
    """
    select_string = """
                SELECT * FROM section
                """
    try:
        result = connexion.DB.execute(select_string)
        res = []
        for row in result:
            r = Section.from_dict(row)
            res.append({
                'CRN': row["CRN"],
                'class_dept': row["class_dept"],
                'class_number': row["class_number"],
                'professor': row["professor"],
                'capacity': row["capacity"],
                'registered': row["registered"]
            })
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500

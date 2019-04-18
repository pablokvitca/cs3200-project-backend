import connexion
import six

from swagger_server.models.class_prereq_group import ClassPrereqGroup  # noqa: E501
from swagger_server import util

from sqlalchemy import types
from sqlalchemy import exc


def get_class_prereqs(class_department, class_number):  # noqa: E501
    """Lists prereqs for the given class

    Returns a prereqs for the given class # noqa: E501

    :param class_department: short code of the Department related to the Class related to the ClassPrereqGroup to return
    :type class_department: str
    :param class_number: number of the Class related to the ClassPrereqGroup to return
    :type class_number: int

    :rtype: None
    """
    def insert_group_deep(g, pgc_group_id, pgc_min_fulfilled_req,
                          pgc_parent_group_id, pgc_class_dept,
                          pgc_class_number, pc_class_dept, pc_class_number, pc_id):
        if g["group_id"] == pgc_group_id:
            if not isinstance(pc_id, type(None)):
                g["reqs"].append({
                    "class_dept": pc_class_dept,
                    "class_number": pc_class_number,
                    "id": pc_id
                })
        elif g["group_id"] == pgc_parent_group_id:
            n_req = {
                "group_id": pgc_group_id,
                "min_fulfilled_req": pgc_min_fulfilled_req,
                "parent_group_id": pgc_parent_group_id,
                "reqs": []
            }
            if not isinstance(pc_id, type(None)):
                n_req["reqs"].append({
                        "class_dept": pc_class_dept,
                        "class_number": pc_class_number,
                        "id": pc_id
                    })
            g["reqs"].append(n_req)
        elif "reqs" in g:
            for r in g["reqs"]:
                insert_group_deep(r,
                                  pgc_group_id, pgc_min_fulfilled_req,
                                  pgc_parent_group_id, pgc_class_dept,
                                  pgc_class_number, pc_class_dept, pc_class_number, pc_id)

    try:
        db_conn = connexion.DB_ENG.raw_connection()
        cursor = db_conn.cursor()
        cursor.callproc("select_prerequisites_recursive", [class_department, class_number])
        db_conn.close()
        res = {}
        for pgc_group_id, pgc_min_fulfilled_req, \
            pgc_parent_group_id, pgc_class_dept, pgc_class_number, \
            pc_class_dept, pc_class_number, pc_id \
                in cursor.fetchall():
            if isinstance(pgc_parent_group_id, type(None)) and "group_id" not in res:
                res["group_id"] = pgc_group_id
                res["min_fulfilled_req"] = pgc_min_fulfilled_req
                res["parent_group_id"] = pgc_parent_group_id
                res["class_dept"] = pgc_class_dept
                res["class_number"] = pgc_class_number
                res["reqs"] = []
            insert_group_deep(res, pgc_group_id, pgc_min_fulfilled_req,
                              pgc_parent_group_id, pgc_class_dept,
                              pgc_class_number, pc_class_dept, pc_class_number, pc_id)
        return res, 200
    except exc.IntegrityError:
        return "Internal Server Error", 500

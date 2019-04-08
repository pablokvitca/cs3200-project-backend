import connexion
import six

from swagger_server.models.pursued_degree import PursuedDegree  # noqa: E501
from swagger_server import util

from swagger_server import encoder

from sqlalchemy import types
from sqlalchemy import exc

from flask import make_response


def add_pursued_degree(body):  # noqa: E501
    """Add a pursued_degree to the classdeck

     # noqa: E501

    :param body: PursuedDegree object that needs to be added to the system
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PursuedDegree.from_dict(connexion.request.get_json())  # noqa: E501
        insert_string = """
            INSERT INTO pursued_degree (
                NUID,
                degree_ID)
            VALUES ({0}, {1});
            """.format(body.nuid, body.degree_id)
        try:
            session_cookie = connexion.request.cookies.get("session")
            session_NUID = connexion.JWT_verify(session_cookie)
            if session_NUID == str(body.nuid).zfill(9):
                connexion.DB.execute(insert_string)
                return "Accepted", 201
            else:
                return "Forbidden", 403
        except exc.IntegrityError as err:
            return "Could not add pursued degree", 406
        except KeyError:
            return "Forbidden", 403
    return "Bad Request", 400


def delete_pursued_degree(nuid, degree_id, tries:int=0):  # noqa: E501
    """Deletes a pursued_degree

     # noqa: E501

    :param nuid: nuid of the user related to the pursued_degree to return
    :type nuid: int
    :param degree_id: nuid of the degree related to the pursued_degree to return
    :type degree_id: int

    :rtype: None
    """
    def retry():
        if tries < 5:
            return delete_pursued_degree(nuid, degree_id, tries + 1)
        else:
            return "I'm Done", 420

    delete_string = "DELETE FROM pursued_degree WHERE nuid = {0} AND degree_id = {1};".format(nuid, degree_id)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        if session_NUID == str(nuid).zfill(9):
            connexion.DB.execute(delete_string)
            return "Accepted", 201
        else:
            return "Forbidden", 403
    except exc.IntegrityError:
        return "Could not add pursued degree", 406
    except exc.InterfaceError:
        retry()
    except exc.OperationalError:
        retry()
    except exc.InternalError:
        retry()
    except KeyError:
        return "Forbidden", 403


def get_pursued_degree_by_nuid(nuid, tries=0):  # noqa: E501
    """List pursued_degree by NUID

    Returns the pursued_degrees related to the given NUID # noqa: E501

    :param nuid: nuid of the user related to the pursued_degree to return
    :type nuid: int

    :rtype: None
    """
    def retry():
        if tries < 5:
            return get_pursued_degree_by_nuid(nuid, tries + 1)
        else:
            return "INTERNAL SERVER ERROR", 500
    select_string = """
        SELECT * FROM pursued_degree
        WHERE
            nuid = {};
        """.format(nuid)
    try:
        session_cookie = connexion.request.cookies.get("session")
        session_NUID = connexion.JWT_verify(session_cookie)
        if session_NUID == str(nuid).zfill(9):
            result = connexion.DB.execute(select_string)
            res = []
            for nuid, degree_id in result.fetchall():
                r = PursuedDegree(nuid, degree_id)
                res.append(r)
            return res, 201
        else:
            return "Forbidden", 403
    except exc.IntegrityError as err:
        return "Could not add pursued degree", 406
    except KeyError:
        return "Forbidden", 403
    except:
        return retry()

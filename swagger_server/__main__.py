#!/usr/bin/env python3
import connexion
from sqlalchemy.engine import Engine

from swagger_server import encoder
import sqlalchemy
from sqlalchemy import create_engine
import json
import six
from werkzeug.exceptions import Unauthorized
from jose import JWTError, jwt
import time
from flask_cors import CORS

settings = {
    # The name of the MySQL account to use (or empty for anonymous)
    'userName': "root",
    # The password for the MySQL account (or empty for anonymous)
    'password': "rycbar12345",
    'serverName': "127.0.0.1",    # The name of the computer running MySQL
    # The port of the MySQL server (default is 3306)
    'portNumber': 3306,
    # The name of the database we are testing with (this default is installed with MySQL)
    'dbName': "projectcs3200",
}

JWT_ISSUER = 'com.classdeck.classdeck'
JWT_SECRET = 'classdeck_JWT_secret'
JWT_LIFETIME_SECONDS = 60 * 60 * 24
JWT_ALGORITHM = 'HS256'


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ClassDeck Project'})
    connexion.DB_ENG = get_db_engine()
    connexion.DB = get_db_connection
    connexion.JWT_verify = verify_jwt
    connexion.JWT_generate_token = generate_token
    connexion.cors = CORS(app.app, supports_credentials=True)
    app.run(port=8080)


def verify_jwt(cookie):
    """If the user is log in is valid, then returns the user id
    else, returns False
    """
    if cookie == 'logged_out':
        return False
    try:
        decoded = decode_token(cookie)
        return decoded["sub"]
    except Unauthorized:
        return False


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def _current_timestamp():
    return int(time.time())


def get_db_connection(eng: Engine):
    return eng.connect()


def get_db_engine():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    db_engine = create_engine(
        'mysql+pymysql://{0[userName]}:{0[password]}@{0[serverName]}:{0[portNumber]}/{0[dbName]}'.format(settings),
        isolation_level="READ_COMMITTED")
    return db_engine


def test_db_connection_db(db) -> bool:
    print('Trying to connect to database')
    # try:
    db_conn = db.connect()
    print('Connected to database')
    db_conn.close()
    return True
    # except Exception as e: ## TODO
    #     print('Error connecting to database. Please check your config.')
    #     return False


# Startup the server:
if __name__ == '__main__':
    main()

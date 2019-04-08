#!/usr/bin/env python3
import connexion
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
    connexion.DB_ENG = get_db()
    connexion.DB = connect_db(get_db())
    connexion.JWT_verify = verify_JWT
    connexion.JWT_generate_token = generate_token
    cors = CORS(app.app, supports_credentials=True)
    app.run(port=8080)


def verify_JWT(cookie):
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


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    db_engine = create_engine(
        'mysql+pymysql://{0[userName]}:{0[password]}@{0[serverName]}:{0[portNumber]}/{0[dbName]}'.format(settings))
    return db_engine


def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db_conn'):
        g.db_conn.close()


def connect_db(db):
    print('Trying to connect to database')
    db_conn = db.connect()
    print('Connected to database')
    return db_conn


if __name__ == '__main__':
    main()

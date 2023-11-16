#!/usr/bin/env python3
""" A function to salt and hash a password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ A function that hash passwords
    """
    bytes_format = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pswd = bcrypt.hashpw(bytes_format, salt)
    return hash_pswd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method to register user
        """
        try:
            user_found = self._db.find_user_by(email=email)
            if user_found is not None:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_pswd = _hash_password(password)
            self._db.add_user(email, hashed_pswd)

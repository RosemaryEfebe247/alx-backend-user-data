#!/usr/bin/env python3
""" A function to salt and hash a password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    """ A function that hash passwords
    """
    bytes_format = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(bytes_format, salt)
    return hash_password


def _generate_uuid() -> str:
    """ A private method to generate UUID
    """
    return str(uuid.uuid4())


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
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ Return True if email exists and matches the password
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                hashed_pswd = user.hashed_password
                if bcrypt.checkpw(password.encode('utf-8'), hashed_pswd):
                    return True
                return False
            return False
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ Method used to retrieve a session
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Method that gets user from session
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            if not user:
                return None
        except Exception:
            return None
        return user

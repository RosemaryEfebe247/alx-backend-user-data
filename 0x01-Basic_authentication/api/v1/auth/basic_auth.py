#!/usr/bin/env python3
""" A class that perfoms basic authentication
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ A basic authentication class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ A method that that extracts the basic header encoding
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ A method that decodes the autorization header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ A method that returns a user email and password
        """
        if decoded_base64_authorization_header is None:
            return(None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        parts = decoded_base64_authorization_header.split(':')
        if len(parts) == 2:
            return (parts[0], parts[1])
        else:
            return (None, None)

    def user_object_from_credentials(
            self, user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ A method that returns the user instance
        """
        if user_email or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
                return None
        users = User.search({'email': user_email})
        if not users:
            return None
        found_user = users
        if not found_user.is_valid_password(user_pwd):
            return None
        return found_user

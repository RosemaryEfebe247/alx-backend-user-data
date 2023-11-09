#!/usr/bin/env python3
""" A class that perfoms basic authentication
"""
from api.v1.auth.auth import Auth
import base64


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

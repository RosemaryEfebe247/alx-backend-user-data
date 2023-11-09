#!/usr/bin/env python3
""" The class to manage API authentication
"""
from models.user import User
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class that handles authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return False
        """
        if path is None or excluded_paths is None:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None
        """
        return None

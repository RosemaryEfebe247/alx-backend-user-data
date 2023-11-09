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
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if fnmatch.fnmatch(path, excluded_path):
                    return False
            elif path == excluded_path or (
                    excluded_path.endswith('/') and path == excluded_path[:-1]
                    ):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return None
        """
        if request is None:
            return None
        authorization_header = request.headers.get('Authorization')
        if authorization_header is None:
            return None
        return authorization_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None
        """
        return None

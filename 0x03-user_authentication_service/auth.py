#!/usr/bin/env python3
""" A function to salt and hash a password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ A function that hash passwords
    """
    bytes_format = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pswd = bcrypt.hashpw(bytes_format, salt)
    return hash_pswd

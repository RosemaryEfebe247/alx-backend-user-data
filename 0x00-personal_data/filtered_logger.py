#!/usr/bin/env python3
"""A function called filter_datum that returns the log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    for item in fields:
        message = re.sub(fr'{re.escape(item)}=.*?(?={re.escape(separator)}|$)',
                         f'{item}={redaction}', message)
    return message

#!/usr/bin/env python3
"""A function called filter_datum that returns the log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ The function uses re.sub to replace items"""
    for field in fields:
        pattern = re.escape(field)
        return (re.sub(fr'{pattern}=.*?(?={re.escape(separator)}|$)',
                       f'{field}={redaction}', message))

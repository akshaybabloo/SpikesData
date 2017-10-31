"""
Utilities that would be used internally for SpikesData.
"""

import sys

__all__ = ['is_windows', 'is_linux', 'is_mac', 'is_python3', 'SplitDataException', 'NotEnoughDataError',
           'ConfigFileNotFound']


def is_windows():
    """
    Check if windows os

    >>> print(is_windows())
    True or False

    Returns
    -------
    bool: bool
        True or False.

    """
    if sys.platform == 'win32':
        return True
    return False


def is_mac():
    """
    Check if mac os

    >>> print(is_mac())
    True or False

    Returns
    -------
    bool: bool
        True or False.

    """
    if sys.platform == 'darwin':
        return True
    return False


def is_linux():
    """
    Check if linux os

    >>> print(is_linux())
    True or False

    Returns
    -------
    bool: bool
        True or False.

    """
    if sys.platform == 'linux':
        return True
    return False


def is_python3():
    """
    Check for Python 3

    >>> print(is_python3())
    True or False

    Returns
    -------
    bool: bool
        True or False
    """
    if sys.version_info[:2] >= (3, 5):
        return True
    else:
        return False


####################################################################
#                                                                  #
#                           Exceptions                             #
#                                                                  #
####################################################################


class NotEnoughDataError(Exception):
    def __init__(self, message, errors=None):
        super(NotEnoughDataError, self).__init__(message)

        self.errors = errors


class SplitDataException(Exception):
    def __init__(self, message, errors=None):
        super(SplitDataException, self).__init__(message)

        self.errors = errors


class ConfigFileNotFound(Exception):
    def __init__(self, message, errors=None):
        super(ConfigFileNotFound, self).__init__(message)

        self.errors = errors

"""This module provides a Failure class to handle Exceptions"""

class Failure(Exception):
    """Failure exception"""
    def __init__(self,value):
        """Initializes failure"""
        self.value=value
    def __str__(self):
        """String that gets written out when exception occurs"""
        return repr(self.value)

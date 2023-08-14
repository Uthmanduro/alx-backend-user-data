#!/usr/bin/env python3
"""module to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the authentication API"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns true if path is not in excluded_paths"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """method that handles authorization header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """method that handles current user"""
        return None

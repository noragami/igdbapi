#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import sys
from collections import namedtuple
from enum import Enum
from argparse import Namespace

import requests

from . import errors
from .decorators import Singleton

V1_ENDPOINT = "https://igdbcom-internet-game-database-v1.p.mashape.com/"
VALID_RESOURCES = ['games', 'companies', 'people', 'franchises', 'platforms']


@Singleton
class APIClient(object):

    def __init__(self, api_key=None):
        self._api_key = api_key
        self._command = None
        self._headers = {'Accept': 'application/json; charset=UTF-8', 'X-Mashape-Key': self._api_key}

        if api_key is None:
            raise ValueError('You must set an API key.')

    def call(self, command, params):

        self._command = command

        print('command is ' + command)

        # if command not in VALID_RESOURCES:
        #    raise ValueError('API command {command} is not valid.'.format(command=command))

        base_url = str(self)

        response = requests.request('GET', base_url,
                                    params=params,
                                    headers=self._headers, allow_redirects=False)

        print(response.url, response.status_code)
        # print(response.status_code)
        # print(response.json())

        errors.check(response)

        return APIResponse(response.text)

    @property
    def command(self):
        return self._command

    @property
    def api_key(self):
        return self._api_key

    @property
    def headers(self):
        return self._headers

    def __str__(self):
        return '{endpoint}{resource}'.format(endpoint=V1_ENDPOINT, resource=self._command)


class APIResponse(object):

    def __init__(self, response):
        # Parse JSON into an object with attributes corresponding to dict keys.
        self._response = response

    def single_result(self):
        if type(self.json_response()) == list:
            if len(self.json_response()) == 1:
                return self.json_response()[0]
            else:
                raise errors.APIError('Expected single result, found {results}'.format(results=len(self._response)))
        return self.json_response()

    def collection_result(self):
        return self.json_response()

    @staticmethod
    def _json_object_hook(d):
        return Namespace(**d)

    def json2obj(self, data):
        return json.loads(data, object_hook=self._json_object_hook)

    def json_response(self):
        return self.json2obj(self._response)

    @property
    def response(self):
        return self._response


class FilterPostFix(Enum):
    """
    eq Equal: Exact match equal.
    not_eq Not Equal: Exact match equal.
    gt Greater than works only on numbers.
    gte Greater than or equal to works only on numbers.
    lt Less than works only on numbers.
    lte Less than or equal to works only on numbers.
    prefix Prefix of a value only works on strings.
    exists The value is not null.
    not_exists The value is null.
    in The value exists within the (comma separated) array.
    """
    Equal = 'eq'
    Not_Equal = 'not_eq'
    Greater_than = 'gt'
    Greater_than_or_equal = 'gte'
    Less_than = 'lt'
    Less_than_or_equal = 'lte'
    Prefix = 'prefix'
    Not_Null = 'exists'
    Null = 'not_exists'
    Within = 'in'

    def __str__(self):
        return self.value


class Filter(namedtuple('filter', 'key, postfix, value')):

    def to_param(self):
        return {'filter[{}][{}]'.format(self.key, str(self.postfix)): self.value}

"""
class Filter(object):

    def __init__(self, key, value, postfix=FilterPostFix.Equal):
        self._key = key
        self._postfix = postfix
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def postfix(self):
        return str(self._postfix)

    @property
    def value(self):
        return self._value
"""

class APIObject(object):
    """
    A base class for all rich Igdb objects.
    """

    @property
    def id(self):
        return self._id  # "_id" is set by the child class.

    def __repr__(self):
        try:
            return '<{clsname} "{name}" ({id})>'.format(clsname=self.__class__.__name__,
                                                        name=_shims.sanitize_for_console(self._name),
                                                        id=self._id)
        except AttributeError:
            return '<{clsname} ({id})>'.format(clsname=self.__class__.__name__, id=self._id)

    def __eq__(self, other):
        """
        :type other: SteamObject
        """
        # Use a "hash" of each object to prevent cases where derivative classes sharing the
        # same ID, like a user and an app, would cause a match if compared using ".id".
        return hash(self) == hash(other)

    def __ne__(self, other):
        """
        :type other: SteamObject
        """
        return not self == other

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def print_date(date):
        return datetime.datetime.fromtimestamp(date).strftime('%c')


class _shims:
    """
    A collection of functions used at junction points where a Python 3.x solution potentially degrades functionality
    or performance on Python 2.x.
    """

    class Python2:
        @staticmethod
        def sanitize_for_console(string):
            """
            Sanitize a string for console presentation. On Python 2, it decodes Unicode string back to ASCII, dropping
            non-ASCII characters.
            """
            return string.encode(errors="ignore")

    class Python3:
        @staticmethod
        def sanitize_for_console(string):
            """
            Sanitize a string for console presentation. Does nothing on Python 3.
            """
            return string

    if sys.version_info.major >= 3:
        sanitize_for_console = Python3.sanitize_for_console
    else:
        sanitize_for_console = Python2.sanitize_for_console

    sanitize_for_console = staticmethod(sanitize_for_console)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum

from .core import APIObject, APIClient


class Games(APIObject):

    def find(self, id, fields='*'):
        params = {
            'fields': fields
        }
        return APIClient().call(command='games/{id}'.format(id=id), params=params).as_single_result()

    def search(self, search=None, filters=None, fields='*', limit=10, offset=0, order=None):
        if type(fields) is list:
            fields = ','.join(map(str, fields))

        params = {
            'fields': fields,
            'limit': limit,
            'offset': offset,
            'order': order,
        }

        if search is not None:
            params.update({'search': search})

        if filters is not None:
            if type(filters) is list:
                for item in filters:
                    params.update(item.to_param())
            else:
                params.update(filters.to_param())

        return APIClient().call(command='games/', params=params).as_collection()

    def meta(self):
        return APIClient().call(command='games/meta', params={}).as_collection()

    def all(self, fields='*', limit=10, offset=0, order=None):
        limit = min(max(limit, 0), 50)
        return self.search(self, fields, limit, offset, order)


class ESRB(Enum):
    """
    1	RP
    2	EC
    3	E
    4	E10+
    5	T
    6	M
    7	AO
    """
    RP = 1
    EC = 2
    E = 3
    E10plus = 4
    T = 5
    M = 6
    AO = 7

    def __str__(self):
        return self.value


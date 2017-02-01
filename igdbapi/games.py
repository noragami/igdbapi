#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core import APIObject, APIClient


class Games(APIObject):

    def find(self, id, fields='*'):
        params = {
            'fields': fields
        }
        return APIClient().call(command='games/{id}'.format(id=id), params=params).single_result()

    def search(self, search, filters=None, fields='*', limit=10, offset=0, order=None):
        if type(fields) is list:
            fields = ','.join(map(str, fields))

        params = {
            'fields': fields,
            'limit': limit,
            'offset': offset,
            'order': order,
            'search': search
        }

        if filters is not None:
            if type(filters) is list:
                for item in filters:
                    params.update(item.to_param())
            else:
                params.update(filters.to_param())

        return APIClient().call(command='games/', params=params).collection_result()

    def meta(self):
        return APIClient().call(command='games/meta', params={}).collection_result()


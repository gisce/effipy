# -*- coding: utf-8 -*-
from datetime import datetime
from libsaas import http, parsers
from libsaas.services import base

from . import resource


class Measures(resource.EffiPeopleResource):
    """Permite gestionar las medidas.
    """
    path = 'measures'

    @base.apimethod
    def get(self, usagePointId, meterId, date, period, measureType,
            limit=None, offset=None):
        # if date is an instance of datetime, convert it to a unix epoch
        if isinstance(date, datetime):
            date = date.strftime('%s')
        params = base.get_params(('usagePointId', 'meterId', 'date', 'period',
                                  'measureType', 'limit', 'offset'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def delete(self, usagePointId, meterId, date, period, measureType):
        # if date is an instance of datetime, convert it to a unix epoch
        if isinstance(date, datetime):
            date = date.strftime('%s')
        params = base.get_params(('usagePointId', 'meterId', 'date', 'period',
                                  'measureType'), locals())
        request = http.Request('DELETE', self.get_url(), params)

        return request, parsers.parse_empty

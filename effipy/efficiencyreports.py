# -*- coding: utf-8 -*-
from libsaas.services import base
from libsaas import http, parsers

from . import resource


class EfficiencyReports(resource.EffiPeopleResource):
    """Obtiene el informe energético progresivo para una contrato en una fecha.
    """
    path = 'efficiencyreports'

    @base.apimethod
    def get(self, contractId, dateTime):
        params = base.get_params(('contractId', 'dateTime'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def create(self, obj):
        raise base.MethodNotSupported()

    @base.apimethod
    def update(self, obj):
        raise base.MethodNotSupported()

    @base.apimethod
    def delete(self):
        raise base.MethodNotSupported()

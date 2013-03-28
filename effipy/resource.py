from libsaas import http, parsers
from libsaas.services import base


class EffiPeopleResource(base.RESTResource):

    @base.apimethod
    def get(self, start=None, limit=None):
        params = base.get_params(('start', 'limit'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def update(self, obj):
        self.require_item()
        request = http.Request('PUT', self.get_url(), self.wrap_object(obj))

        return request, parsers.parse_json

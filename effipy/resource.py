from libsaas import http, parsers
from libsaas.services import base


class EffiPeopleResource(base.RESTResource):

    @base.apimethod
    def get(self, start=None, limit=None):
        """
        .. py:function:: get
         `get()` method for all the EffiPeople resources.
        
        :param int start: Start of the results
        :param int limit: Limit of the results
        """
        params = base.get_params(('start', 'limit'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def update(self, obj):
        self.require_item()
        request = http.Request('PUT', self.get_url(), self.wrap_object(obj))

        return request, parsers.parse_json

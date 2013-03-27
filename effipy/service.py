from libsaas.filters import auth
from libsaas.services import base

from . import customers


class EffiPeople(base.Resource):
    """
    """
    def __init__(self, token, version='v1', test=False):
        self.token = token
        if test:
            endpoint = "http://effipeople-api-staging.azurewebsites.net"
        else:
            endpoint = "https://api.effipeople.com"
        self.apiroot = '%s/%s' % (endpoint, version)
        self.add_filter(auth.BasicAuth(token, ''))

    def get_url(self):
        return self.apiroot

    @base.resource(customers.Customers)
    def customer(self, customer_id):
        return customers.Customers(self, customer_id)

    @base.resource(customers.Customers)
    def customers(self):
        return customers.Customers(self)

"""
effipy.service
~~~~~~~~~~~~~~

:copyrigth: (c) 2013 by GISCE-TI, S.L. See AUTHORS for more details.
:licese: GPL2, see LICENSE for more details.
"""


import json

from libsaas import http
from libsaas.filters import auth
from libsaas.services import base

from . import customers, usagepoints, efficiencyreports, measures, tariffs


class EffiPeople(base.Resource):
    """
    EffiPeople Service API.
    """
    def __init__(self, token, version='v1', test=False):
        """
        Initializes the EffiPeople service.

        You must pass the ``token`` for this service.

        >>> from effipy import EffiPeople
        >>> ef = EffiPeople(token='34234fasdfas2343fsdfa')
        >>> ef.apiroot
        >>> 'https://api.effipeople.com/v1'
        >>> ef = EffiPeople(token='34234fasdfas2343fsdfa', version='v2')
        >>> ef.apiroot
        >>> 'https://api.effipeople.com/v2'
        """
        self.token = token
        if test:
            endpoint = "https://effipeople-api-staging.azurewebsites.net"
        else:
            endpoint = "https://api.effipeople.com"
        self.apiroot = '%s/%s' % (endpoint, version)
        self.add_filter(self.use_json)
        self.add_filter(auth.BasicAuth(token, ''))

    def use_json(self, request):
        if request.method.upper() not in http.URLENCODE_METHODS:
            request.headers['Content-Type'] = 'application/json'
            request.params = json.dumps(request.params)

    def get_url(self):
        return self.apiroot

    @base.resource(customers.Customers)
    def customer(self, customer_id):
        """Specific ``Customer`` in :class:`effipy.customers.Customers`.

        >>> from effipy import EffiPeople
        >>> ef = EffiPeople(token='XXXXX')
        
        Customers
        
        >>> ef.customer(1234).get_url()
        'https://api.effipeople.com/v1/customers/1234'
        
        Contracts
        
        >>> ef.customer(1234).contracts().get_url()
        'https://api.effipeople.com/v1/customers/1234/contracts'
        >>> ef.customer(1234).contract(1).get_url()
        'https://api.effipeople.com/v1/customers/1234/contracts/1'
        >>> ef.customer(1234).contract(1).versions().get_url()
        'https://api.effipeople.com/v1/customers/1234/contracts/1/versions'
        >>> ef.customer(1234).contract(1).version(1).get_url()
        'https://api.effipeople.com/v1/customers/1234/contracts/1/versions/1'
        
        Invoices
        
        >>> ef.customer(1234).contract(1).invoices().get_url()
        'https://api.effipeople.com/v1/customers/1234/contracts/1/invoices'
        >>> ef.customer(1234).contract(1).invoice(1).get_url()
        'https://api.effipeople.com/v1/customers/1234/contracts/1/invoices/1'
        """
        return customers.Customers(self, customer_id)

    @base.resource(customers.Customers)
    def customers(self):
        """Endpoint to ``Customers`` in :class:`effipy.customers.Customers`.

        >>> from effipy import EffiPeople
        >>> ef = EffiPeople(token='XXXXX')
        >>> ef.customers().get_url()
        'https://api.effipeople.com/v1/customers'
        """
        return customers.Customers(self)

    @base.resource(usagepoints.UsagePoints)
    def usagepoint(self, point_id):
        """Endpoint to specific UsagePoint :class:`effipy.usagepoints.Usagepoints`.

        >>> from effipy import EffiPeople
        >>> ef = EffiPeople(token='XXXXX')
        >>> ef.usagepoint('ES00001111').get_url()
        'https://api.effipeople.com/v1/usagepoints/ES00001111'
        """
        return usagepoints.UsagePoints(self, point_id)

    @base.resource(usagepoints.UsagePoints)
    def usagepoints(self):
        """Endpoint to UsagePoints.

        >>> from effipy import EffiPeople
        >>> ef = EffiPeople(token='XXXXX')
        >>> ef.usagepoints().get_url()
        'https://api.effipeople.com/v1/usagepoints'
        """
        return usagepoints.UsagePoints(self)

    @base.resource(measures.Measures)
    def measure(self, measure_id):
        return measures.Measures(self, measure_id)

    @base.resource(measures.Measures)
    def measures(self):
        return measures.Measures(self)

    @base.resource(efficiencyreports.EfficiencyReports)
    def efficiency_reports(self):
        return efficiencyreports.EfficiencyReports(self)

    @base.resource(tariffs.Tariffs)
    def tariff(self, tariff_id):
        """Endpoint to Tariff :class:`effipy.tariffs.Tariffs`.

        >>> from effipy import EffiPeople
        >>> ef = EffiPeople(token='XXXXX')
        >>> ef.tariff('T1').get_url()
        'https://api.effipeople.com/v1/tariffs/T1'
        >>> ef.tariff('T1').versions().get_url()
        'https://api.effipeople.com/v1/tariffs/T1/versions'
        >>> ef.tariff('T1').version('V1').get_url()
        'https://api.effipeople.com/v1/tariffs/T1/versions/V1'
        """
        return tariffs.Tariffs(self, tariff_id)

    @base.resource(tariffs.Tariffs)
    def tariffs(self):
        return tariffs.Tariffs(self)

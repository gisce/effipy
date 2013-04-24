import json

from libsaas import http
from libsaas.filters import auth
from libsaas.services import base

from . import customers, meters, usagepoints, efficiencyreports, measures


class EffiPeople(base.Resource):
    """
    """
    def __init__(self, token, version='v1', test=False):
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
        return customers.Customers(self, customer_id)

    @base.resource(customers.Customers)
    def customers(self):
        return customers.Customers(self)

    @base.resource(meters.Meters)
    def meter(self, meter_id):
        return meters.Meters(self, meter_id)

    @base.resource(usagepoints.UsagePoints)
    def usagepoint(self, point_id):
        return usagepoints.UsagePoints(self, point_id)

    @base.resource(usagepoints.UsagePoints)
    def usagepoints(self):
        return usagepoints.UsagePoints(self)

    @base.resource(measures.Measures)
    def measure(self, measure_id):
        return measures.Measures(self, measure_id)

    @base.resource(measures.Measures)
    def measures(self):
        return measures.Measures(self)

    @base.resource(efficiencyreports.EfficiencyReports)
    def efficiency_reports(self):
        return efficiencyreports.EfficiencyReports()

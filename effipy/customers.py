# -*- coding: utf-8 -*-
from libsaas.services import base

from . import resource
from . import contracts


class Customers(resource.EffiPeopleResource):
    """
    Customers management

    Use ``object_id`` to get the endpoint to a escpecific customer.
    """
    path = 'customers'

    @base.resource(contracts.Contracts)
    def contract(self, object_id):
        return contracts.Contracts(self, object_id)

    @base.resource(contracts.Contracts)
    def contracts(self):
        return contracts.Contracts(self)

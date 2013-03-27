# -*- coding: utf-8 -*-
from libsaas.services import base

from . import resource
from . import contracts


class Customers(resource.EffiPeopleResource):
    """Permite gestionar los clientes de la compañía.
    """
    path = 'customers'

    @base.resource(contracts.Contracts)
    def contract(self, object_id):
        return contracts.Contracts(self, object_id)

    @base.resource(contracts.Contracts)
    def contracts(self):
        return contracts.Contracts(self)

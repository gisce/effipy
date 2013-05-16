# -*- coding: utf-8 -*-
from libsaas.services import base

from . import resource
from . import invoices as _invoices


class ContractsVersions(resource.EffiPeopleResource):
    """Permite gestionar las versions de los contratos.
    """
    path = 'versions'


class Contracts(resource.EffiPeopleResource):
    """Permite gestionar los contratos de los clientes de la compañía.
    """
    path = 'contracts'

    @base.resource(ContractsVersions)
    def version(self, object_id):
        return ContractsVersions(self, object_id)

    @base.resource(ContractsVersions)
    def versions(self):
        return ContractsVersions(self)

    @base.resource(_invoices.Invoices)
    def invoice(self, object_id):
        return  _invoices.Invoices(self, object_id)

    @base.resource(_invoices.Invoices)
    def invoices(self):
        return  _invoices.Invoices(self)

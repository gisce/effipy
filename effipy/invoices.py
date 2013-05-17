# -*- coding: utf-8 -*-
from libsaas.services import base

from . import resource
from . import invoice_measures


class Invoices(resource.EffiPeopleResource):
    path = 'invoices'

    @base.resource(invoice_measures.InvoiceMeasures)
    def measure(self, measure_id):
        return invoice_measures.InvoiceMeasures(self, measure_id)

    @base.resource(invoice_measures.InvoiceMeasures)
    def measures(self):
        return invoice_measures.InvoiceMeasures(self)

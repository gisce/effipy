# -*- coding: utf-8 -*-
from libsaas.services import base

from . import resource


class Versions(resource.EffiPeopleResource):
    """Permite gestionar las versions de las tarifas.
    """
    path = 'versions'


class Tariffs(resource.EffiPeopleResource):
    """Permite gestionar las tarifas de la compañía.
    """
    path = 'tariffs'

    @base.resource(Versions)
    def version(self, object_id):
        return Versions(self, object_id)

    @base.resource(Versions)
    def versions(self):
        return Versions(self)

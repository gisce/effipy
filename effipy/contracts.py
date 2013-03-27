# -*- coding: utf-8 -*-

from . import resource


class Contracts(resource.EffiPeopleResource):
    """Permite gestionar los contratos de los clientes de la compañía.
    """
    path = 'contracts'

# -*- coding: utf-8 -*-
from . import resource


class Readings(resource.EffiPeopleResource):
    """Permite gestionar las lecturas de un contador
    """
    path = 'readings'

    def __init__(self, parent, object_id, period=None):
        self.parent = parent
        self.object_id = object_id
        self.period = period

    def get_url(self):
        if self.period is None:
            return super(Readings, self).get_url()

        return '{0}/{1}/{2}/{3}'.format(self.parent.get_url(), self.path,
                                        self.object_id, self.period)

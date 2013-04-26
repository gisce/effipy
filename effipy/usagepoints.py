# -*- coding: utf-8 -*-
from libsaas.services import base

from . import resource
from . import meters


class UsagePoints(resource.EffiPeopleResource):
    path = 'usagepoints'

    @base.resource(meters.Meters)
    def meter(self, object_id):
        return meters.Meters(self, object_id)

    @base.resource(meters.Meters)
    def meters(self):
        return meters.Meters(self)

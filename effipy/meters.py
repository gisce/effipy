from libsaas.services import base

from . import resource
from . import readings


class Meters(resource.EffiPeopleResource):
    """Permite gestionar los contadores que realizan las medidas
    """
    path = 'meters'

    @base.resource(readings.Readings)
    def reading(self, reading_datetime, period=None):
        return readings.Readings(self, reading_datetime, period)

    @base.resource(readings.Readings)
    def readings(self):
        return readings.Readings(self)

from django.db import models


class PeriodManager(models.Manager):
    MIDDAY = '12:00'

    def at_morning(self):
        return self.filter(start__lt=self.MIDDAY)

    def at_afternoon(self):
        return self.filter(start__gte=self.MIDDAY)
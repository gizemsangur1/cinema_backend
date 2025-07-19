from django.db import models

from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    seat_rows = models.IntegerField()
    seat_columns = models.IntegerField()

    def __str__(self):
        return self.name


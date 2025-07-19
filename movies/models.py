from django.db import models

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_url = models.URLField()
    duration_minutes = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

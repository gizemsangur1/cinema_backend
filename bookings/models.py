from django.db import models

from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from seats.models import Hall

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} @ {self.hall.name} on {self.datetime}"

class Reservation(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_row = models.IntegerField()
    seat_column = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    reserved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['session', 'seat_row', 'seat_column']


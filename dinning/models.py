from django.db import models
from django.contrib.auth.models import User

class DiningPlace(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dining_place = models.ForeignKey(DiningPlace, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.dining_place.name} on {self.date} at {self.time}"

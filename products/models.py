# from itertools import car
from django.db import models

REVIEW_STARS_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Car(models.Model):
    name = models.CharField(max_length=128)
    picture = models.ImageField(null=True, blank=True )
    price = models.FloatField(max_length=10)
    model = models.CharField(max_length=64, null=True)
    brand = models.CharField(max_length=64, default="unknown")
    description = models.CharField(max_length=256)

    def __str__(self):
         return self.name

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    review = models.CharField(max_length=1024)
    date = models.DateField('review date')

    def __str__(self):
         return "[" + str(self.car) + "] " + self.review[0:32]
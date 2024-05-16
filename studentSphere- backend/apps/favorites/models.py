# favorites/models.py

from django.db import models
from apps.student.models import StudentModel
from apps.apartments.models import Apartment

class Favorite(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.student.first_name}'s Favorite: {self.apartment.name}"

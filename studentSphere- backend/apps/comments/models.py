from django.db import models
from apps.student.models import StudentModel
from apps.apartments.models import Apartment

class Comment(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} - {self.apartment.name}'

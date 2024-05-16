# models.py in your Django app

from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    area = models.CharField(max_length=255)
    bed = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    student_comments = models.TextField()
    stars = models.PositiveIntegerField()
    image_url = models.URLField()
    amenities = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'apartments'
        app_label = 'apartments'  


from django.db import models

class Course(models.Model):
    LEVEL_CHOICES = [
        ('FREE', 'Gratuito'),
        ('PREMIUM', 'Premium'),
    ]
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    level_required = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='FREE')

class Pictogram(models.Model):
    pictogram_id = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)

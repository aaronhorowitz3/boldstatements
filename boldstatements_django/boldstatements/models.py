from datetime import datetime, timedelta, tzinfo
from django.db import models

# Create your models here.
class Statement(models.Model):
    prediction = models.CharField(max_length=500)
    predictor = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='documents/')
    link = models.TextField(blank=True)
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prediction

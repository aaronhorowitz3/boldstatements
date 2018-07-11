from datetime import datetime, timedelta, tzinfo
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Statement(models.Model):
    prediction = models.CharField(max_length=500)
    predictor = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='documents/')
    link = models.TextField(blank=True)
    datestamp = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)
    TRUE = 'T'
    FALSE = 'F'
    CONFIRMATION_CHOICES = (
        (TRUE, 'True'),
        (FALSE, 'False'),
    )
    confirmation = models.CharField(
        max_length=2,
        choices = CONFIRMATION_CHOICES,
        blank=True,
    )
    confirmation_source = models.TextField(blank=True)

    def __str__(self):
        return self.prediction

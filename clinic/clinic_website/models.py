from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    specialization = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.name

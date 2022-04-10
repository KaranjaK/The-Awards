from turtle import title
from django.db import models

# Create your models here.

# This is the Projects model
class Projects(models.Model):
    title = models.CharField(max_length=30)
    
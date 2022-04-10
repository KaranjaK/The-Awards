from turtle import title
from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import CharField

# Create your models here.

# This is the Projects model
class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = CloudinaryField('image')
    projectdesc = models,CharField(max_length=150)
    link = models.CharField(max_length=40)

    # It will create the Project model and convert its inputs into a String
    def __str__(self):
        return self.name

    # This is for creating a project into the app
    def save_project(self):
        self.save()
    
    # This is for deleting the project from the app
    def delete_project(self):
        self.delete()
    
    # This is for updating the project in the app
    def update_project(self):
        self.update()
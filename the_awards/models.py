from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.forms import CharField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# User Profile Model
class Profile(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = CloudinaryField('image')
    bio = models.CharField(max_length=40)
    projects = models.CharField(max_length=60)
    contact = models.EmailField(max_length=150, blank=True)

    # This is a method to convert the models input into strings
    def __str__(self):
        return f'{self.owner.username} Profile'

    # Uses post_save to create a profile
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(owner=instance)
    
    # Uses post_save to save the user profile created above
    @receiver(post_save, sende=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

# This is the Projects model
class Projects(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    image = CloudinaryField('image')
    projectdesc = models,CharField(max_length=300)
    link = models.CharField(max_length=40)
    date = models.DateField(auto_now_add=True, blank=True)

    # It will create the Project model and convert its inputs into a String
    def __str__(self):
        return f'{self.title} Projects'

    # This is for creating a project into the app
    def save_project(self):
        self.save()
    
    # This is for deleting the project from the app
    def delete_project(self):
        self.delete()
    
    # Class method to conduct searches
    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    # Class method to access all projects in the db
    @classmethod
    def all_projects(cls):
        return cls.objects.all()
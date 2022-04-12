from os import link
from turtle import title
from django.test import TestCase
from .models import Projects, Profile, Rate, User

# Create your tests here.
# Testing for the project class
class ProjectsTest(TestCase):

    # Creating an instance of the Projects class for testing
    def setUp(self):
        self.user = User(id=1   , username='KK')
        self.project = Projects(id=1,title='Django Unchained',owner=self.user,image='https://www.shutterstock.com/image-photo/picture-beautiful-view',link='https://project.url')
    
    # Testing the instance created
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

    # Testing project save
    def test_save_project(self):
        self.project.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project)>0)

    # Testing project delete
    def test_delete_project(self):
        self.project.delete_project()
        project = Projects.objects.all()
        self.assertTrue(len(project)==0)
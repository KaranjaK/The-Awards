from email.mime import image
from turtle import title
from django.test import TestCase
from .models import Projects

# Create your tests here.
# Testing for the project class
class ProjectsTest(TestCase):

    # Creating an instance of the Projects class for testing
    def setUp(self):
        self.project = Projects('Django unchained','yes.jpg','A project beyond normal','http://unchained.django.com')
        self.project.save_project
    
    # Testing the instance created
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))
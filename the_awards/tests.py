from django.test import TestCase
from .models import Projects, Profile, Rate

# Create your tests here.
# Testing for the project class
class ProjectsTest(TestCase):

    # Creating an instance of the Projects class for testing
    def setUp(self):
        self.project = Projects('Django unchained','yes.jpg','A project beyond normal','http://unchained.django.com', 7.7, 'Awesome dimension')
        self.project.save_project
    
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
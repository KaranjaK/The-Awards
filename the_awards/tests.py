from django.test import TestCase
from .models import Projects, Profile, Rate, User

# Create your tests here.
# Testing the Profile class
class ProfileTest(TestCase):

    # Creating an instance of a profile in the tests db
    def setUp(self):
        self.user = User(id=1,username='kk', password='wewe1234')
    
    # Testing the instance of the user
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
    
    # Testing saving of a user
    def test_save_user(self):
        self.user.save()

    # Testing for deleting a user
    def test_delete_user(self):
        self.user.delete()

# Testing for the project class
class ProjectsTest(TestCase):

    # Creating an instance of the Projects class for testing
    def setUp(self):
        self.user = User(username='kk')
        self.project = Projects(id=1,title='Django Unchained',user=self.user,image='https://www.shutterstock.com/image-photo/picture-beautiful-view',link='https://project.url')
    
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
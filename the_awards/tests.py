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
        user = User.objects.all()
        self.assertTrue(len(user)==0)

# Testing for the project class
class ProjectsTest(TestCase):

    # Creating an instance of the Projects class for testing
    def setUp(self):
        self.user = User(username='kk')
        self.projects = Projects(id=1,title='Django Unchained',user=self.user,image='https://www.shutterstock.com/image-photo/picture-beautiful-view',link='https://project.url')
    
    # Testing the instance created
    def test_instance(self):
        self.assertTrue(isinstance(self.projects, Projects))

    # Testing project save
    def test_save_project(self):
        self.projects.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    # Testing project delete
    def test_delete_project(self):
        self.projects.delete_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)==0)

# Testing the rate model and its methods
class RateTest(TestCase):
    # Setup a project and its related rating
    def setUp(self):
        self.user = User.objects.create(id=1, username='kk')
        self.projects = Projects(id=1,title='Django Unchained',user=self.user,image='https://www.shutterstock.com/image-photo/picture-beautiful-view',link='https://project.url')
        self.rate = Rate.objects.create(id=1, design=8, usability=6, content=4, user=self.user, project=self.projects)
    
    # Check the instance of the rating created above
    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rate))

    # Test if the rating is being saved
    def test_save_rating(self):
        self.rate.save_rating()
        rate = Rate.objects.all()
        self.assertTrue(len(rate) > 0)

    # Test the getting of a rating for display purposes
    def test_get_rating(self, id=1):
        self.rate.save()
        rate = Rate.get_rating(id)
        self.assertTrue(len(rate) == 1)
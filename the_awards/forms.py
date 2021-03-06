from email.mime import image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Projects, Profile, Rate
from cloudinary.models import CloudinaryField


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProjectsForm(forms.ModelForm):
    image = CloudinaryField('image')

    class Meta:
        model = Projects
        fields = ('image', 'title', 'link', 'project_description',)


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'contact']


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content']
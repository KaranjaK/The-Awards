from rest_framework import serializers
from .models import Profile, Projects
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'image', 'bio', 'projects', 'contact']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'title', 'user', 'image', 'projectdesc', 'link', 'date']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    projects = ProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'profile', 'projects']
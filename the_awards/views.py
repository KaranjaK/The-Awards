from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProjectsForm, UpdateUserForm, UpdateUserProfileForm, RateForm
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects, Rate
from .serializers import ProfileSerializer, UserSerializer, ProjectsSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random

# Create your views here.

# The default landing page
def index(request):
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.user = request.user
            projects.save()
    else:
        form = ProjectsForm()

    try:
        projects = Projects.objects.all()
        projects = projects[::-1]
        a_projects = random.randint(0, len(projects)-1)
        random_projects = projects[a_projects]
    except Projects.DoesNotExist:
        projects = None
    return render(request, 'index.html', {'projects': projects, 'form': form, 'random_projects': random_projects})


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit.html', params)


@login_required(login_url='login')
def project(request, projects):
    projects = Projects.objects.get(title=projects)
    ratings = Rate.objects.filter(user=request.user, projects=projects).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.projects = projects
            rate.save()
            projects_ratings = Rate.objects.filter(projects=projects)

            design_ratings = [d.design for d in projects_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in projects_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in projects_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RateForm()
    params = {
        'projects': projects,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'projects.html', params)


def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Projects.objects.filter(title__icontains=title).all()
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework import routers

# Routers definition
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('projects', views.ProjectsViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^(?P<username>\w+)/profile$', views.user_profile, name='userprofile'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profile/(?P<username>\w+)/', views.profile, name='profile'),
    url(r'^profile/(?P<username>\w+)/settings$', views.edit_profile, name='edit'),
    path('projects/<projects>/', views.project, name='projects'),
    url(r'^search/$', views.search_project, name='search'),
]
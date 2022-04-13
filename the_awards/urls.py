from django.conf import settings
from django.conf.urls import url, include
from . import views
from rest_framework import routers

# Routers definition
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('projects', views.ProjectsViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns=[
    url('^$', views.index, name='index'),
    url('^signup/', views.signup, name='signup'),
    url('^account/', include('django.contrib.auth.urls')),
    url('^api/', include(router.urls)),
    url('^<username>/profile$', views.user_profile, name='userprofile'),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^profile/<username>/', views.profile, name='profile'),
    url('^profile/<username>/settings$', views.edit_profile, name='edit'),
    url('^projects/<projects>$', views.project, name='project'),
    url('^search/$', views.search_project, name='search'),
]
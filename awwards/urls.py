from django.urls import path,include
from rest_framework import routers
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.db import router
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('projects', views.PostViewSet)
router.register('userprofiles', views.ProfileViewSet)

urlpatterns = [
    path('',views.home, name='home'),
    path('project/<post>', views.project, name='project'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('search/', views.search_project, name='search'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls), name='api'),
    
]

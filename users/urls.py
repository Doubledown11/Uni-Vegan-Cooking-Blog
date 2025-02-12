from django.shortcuts import render
from django.urls import path, include
from . import views 

# Create your views here.

app_name = 'users'


urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    
    path('blog/', include('blog.urls')),
    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/login_submit/', views.submit_login, name='submit_login'),
    path('logout_user/', views.logout_user, name='logout_user'),

]
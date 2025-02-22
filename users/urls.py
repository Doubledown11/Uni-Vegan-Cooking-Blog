from django.shortcuts import render
from django.urls import path, include
from . import views 
from django.conf.urls.static import static
from django.conf import settings



# Create your views here.

app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('users/', views.sign_up, name='users_to_signup'),

    path('test/', views.test, name='test'),

    path('register/', views.register, name='register'),
    
    path('register/sign_up/', views.sign_up, name='sign_up'),
    #path('register/sign_up/registration/login.html', views.sign_up, name='sign_up'),

    path('login/', views.login, name='login'),
    path('login/login_submit/', views.submit_login, name='submit_login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('account/', views.account, name='account'),

    #paths for contact enquiries below
    path('enquiries/', views.enquiries, name='enquiries'),
    path('make_enquiry/', views.make_enquiry, name='make_enquiry'),

    path('account/account_info_change/', views.account_info_change, name='account_info_change'),
    path('account/account_info_change/account/', views.account, name='account_from_account_change'),
    path('account/change_password_page/', views.change_password_page, name='change_password_page'),
    path('account/change_password_page/change_password/', views.change_password, name='change_password'),
    

    path('account/account/account/change_profile_pic/', views.change_profile_pic, name='change_profile_pic'),

    path('change_profile_pic/', views.change_profile_pic, name='change_profile_pic'),
] 

from django.shortcuts import render
from django.urls import path, include
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from .views import ResetPasswordView

#yutube vid to pass reset
from django.contrib.auth import views as auth_views



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


    # Views for login below 
    path('login/login_submit/', views.submit_login, name='submit_login'),
       
       
    # Trying to do login through auth_views -- has weird bug though where it appends a login_submit on each successful login, so when trying to login again it looks for a wrong URL
    # path('login/', views.login, name='login'),
    # path('login/login_submit/login_submit/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),


   
    path('logout_user/', views.logout_user, name='logout_user'),
    path('forgotten_password/', views.forgotten_password, name='forgotten_password'),
    #path('reset_password/', views.reset_password, name='reset_password'),


    # Below are the URLs used to reset password -- from youtube vid Dennis Ivy
    # we use as_view() since it is a class based view!
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    
    # renders success message and notifies the user that the reset email was sent 
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    # This is the link the user gets in their email, and allows users to open it up through their email and submit a form.
    # uidb64 is the user ID encoded in base 64 encoding, and token is a token to check if that password is valid
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # Shows a password successfully changed message.
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    





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


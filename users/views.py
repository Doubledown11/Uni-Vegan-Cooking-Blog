from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, UpdateUserForm, UploadPhotoForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import User, ProfilePicture, Enquiry
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ContactForm

# Remove below if dont fit in passwo
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


import random


# Create your views here.


### Need to check if users has already been added to the database.
######### Add email anyways, check if email has already been used.
# def sign_up(request):
#     if request.method == 'GET':
#         form = UserCreationForm()
#         return render(request, '', {'form':form})


def test(request):
    return render(request, f'registration/test.html')




def register(request):
    form = RegisterForm()
    return render(request, 'registration/register.html', {"form":form})


def sign_up(request):
    """Register a new user."""

    if request.method == 'POST':
        # Display blank registration form.
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            # Process completed form.
            user = form.save()

            
            user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])


            login(request, user)


            return redirect('users:login')
        

        else:
            print('')

        # else:
        #     print('❌ Form Errors:', form.errors)  # ✅ Debugging
        #     # error_reg = form.error
        #     return render(request, 'registration/login.html', {'form': form, 'error': 'Some fields were left blank or invalid. Try again!'})

    else:
        RegisterForm()

        # # Display a blank or invalid form -- In the case you want to display the form rather than creating one in html
    context = {'form': form}
    return render(request, 'registration/register.html', context)




def account(request):
    enquiries = Enquiry.objects.all().order_by('-created_on')
    print('Enquiries in enquiries_index', enquiries)
    context = {
        'enquiries':enquiries,
    }
    return render(request, 'registration/account.html', context)


def change_password_page(request):
    return render(request, 'registration/change_password.html')


def change_password(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])

        # Check to ensure given password matches whats saved in the database 
        if user.check_password(request.POST['old_password']):
            user.set_password(request.POST['new_password'])
            user.save()
            return render(request, 'registration/account.html')

        else:
            error = 'The old password entered did not match what is saved in the database, please try again!'
            return render(request, 'registration/change_password.html', {'error':error})


def account_info_change(request):
    print('account_info_change called')
    if request.method == 'POST':
        print(request.POST)
        user = User.objects.get(username=request.POST['old_username'])

        # Change Username:
        username_error = ''
        if request.POST['username'] != '':
            if request.POST['username'] == user.username:
                username_error = 'Given username matches what is currently saved'
            else:
                user.username = request.POST['username']

        # Change Email:
        email_error = ''
        if request.POST['email'] != '':
            if request.POST['email'] == user.email:
                email_error = 'Given email matches what is currently saved'
            else:
                user.email = request.POST['email']

        # Change First Name
        first_name_error = ''
        if request.POST['first_name'] != '':
            if request.POST['first_name'] == user.first_name:                
                first_name_error = 'Given first name matches what is currently saved'

            else:
                user.first_name = request.POST['first_name']

        # Change Last Name
        last_name_error = ''
        if request.POST['last_name'] != '':
            if request.POST['last_name'] == user.last_name:
                last_name_error = 'Given last name matches what is currently saved'

            else:
                user.last_name = request.POST['last_name']

        context = {}
     
                
        if username_error != '':
            context['username_error'] = username_error
        
        if email_error != '':
            context['email_error'] = email_error
        
        if first_name_error != '':    
            context['first_name_error'] = first_name_error
        
        if last_name_error != '':
            context['first_name_error'] = last_name_error
        
        # Save Changes
        user.save()   

        # Below won't render my account page again, so I will just route the user to the home page for now
        # return render(request, '/registration/account.html', context)

        return redirect('/users/account/')


def logout_user(request):
    print('logout_user called')
    logout(request)
    return redirect('/')


def login(request): 
    return render(request, 'registration/login.html')



def submit_login(request):
    print('submit login called')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        # print('Form pre valid check')
        # print('LoginForm', form)
        # print('request\n\n', request.POST)
        # print('\n\n')

        # print('form valid?', form.is_valid)

        if form.is_valid():
            # print('Form is valid')
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                user.save()
                login(request, user)
                # print('User Authenticated')
                return redirect('/')
            
            else:
                # TODO: return error to template 
                print('Invalid Login Credentials')
                error = 'Invalid Login Credentials'
                return render('registration/login.html', error)
        
        else:
            print('Errors in form:\n')
            print('login form errors\n\n', form.error_messages)
            print('\n\n\n')
            
            context = form.error_messages
            
            return render(request, 'registration/login.html', context)


        # Below is used for debugging form errors
        # else:
        #     # print errors 
        #     print('form not valid', form.errors)

    else:
        print('else in form called')
        form = LoginForm()


    context = {'form': form}
    return render(request, 'registration/login.html', context)



def forgotten_password(request): 
    """
    Directs the user to the forgotten password template
    """
    context = {} 
    return render(request, 'registration/forgotten_password.html', context)


def account(request):
    enquiries = Enquiry.objects.all().order_by('-created_on')
    print('Enquiries in enquiries_index', enquiries)
    context = {
        'enquiries':enquiries,
    }
    return render(request, 'registration/account.html', context)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    
    #replace success URL with a page which states the email was delivered.
    success_url = reverse_lazy('users/account/')



def reset_password(request, PasswordResetView):
    """
    Sends a password reset email to the user.
    """
    print('reset_password function called')

    email_template_name = 'users/forgotten_password.html'
    subject_template_name = 'users/forgotten_password.html'
    success_message = 'We have emailed you instructions for resetting your password. If an account exists which uses the email given, you should receive an email shortly. Please be sure to check your spam!'
    success_url = reverse_lazy('users:login.html')





def change_profile_pic(request):
    """
    Allows the user to upload/change their profile picture.
    """

    print('media/profile_pics/blank_profile_pic.jpg')
    print('change_profile_pic view called')
    form = UploadPhotoForm()
    print(request.POST)
    print('\n\n\n')


    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid:
            photo = form.cleaned_data['profile_picture']

            # Ensure the user has a profile picture instance
            profile, created = ProfilePicture.objects.get_or_create(user=request.user)
            profile.profile_picture = photo
            profile.save()

            response_data = {'message':'Hello World!'}
            return JsonResponse(response_data)
        
        else:
            form = UploadPhotoForm()
        
    
    print('form\n\n', form)
    return render(request, 'registration/account.html', {'form':form})





def make_enquiry(request): 
    print('Make enquiry function called')
    print('request post', request.POST)

    if request.method == 'POST':
        # Display blank registration form.
        form = ContactForm(data=request.POST)
        
        print('form\n\n', form)
        print('\n\n')
        print('form data', form.data)
        
        print('\n\n')

        if form.is_valid():
            # Process completed form.
            print('form is valid')
            enquiry = form.save()
            return redirect('blog:contact')
            
            
        else:
            print('Form is not valid')
            # print('❌ Form Errors:', form.errors)  # ✅ Debugging

            # print('Form errors', form.error_class)

    else:
        form = ContactForm()

    # context = {'form':form}
   # return render(request, '', context)
        


def enquiries(request):
    print('enquiries function called')
    enquiry = Enquiry.objects.all()
    form = ContactForm()

    print('form', form)

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)

    #     if form.is_valid():
    #         print('enquiries form is valid')

    context = {'enquiry':enquiry}
    print(context)
    return render(request, 'users/account.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, UpdateUserForm, UploadPhotoForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import User 
from django.contrib.auth.models import User

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


"""
Try to use code from below to bring account details to the account page



def blog_detail_responsive(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form" : CommentForm(),
    }
    return render(request, "blog/detail.html", context)


def blog_index_reponsive(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts,
    }
    return render(request, "blog/responsive.html", context)

"""




def account(request):
    return render(request, 'registration/account.html')

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

        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    print('submit login called')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print('Form pre valid check')
        print('LoginForm', form)
        print('request\n\n', request.POST)
        print('\n\n')

        print('form valid?', form.is_valid)

        if form.is_valid():
            print('Form is valid')
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                user.save()
                login(request, user)
                print('User Authenticated')
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




def change_profile_pic(request):
    """
    Allows the user to upload/change their profile picture.
    """

    print('change_profile_pic view called')
    form = UploadPhotoForm()
    print(request.POST)
    print('\n\n\n')
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid:
            photo = form.save(commit=False)
            # Set the uploading user to the users user before upload
            photo.user = request.user

            photo.save()
            return redirect('/')
        

    return render(request, 'registration/account.html', context={'form':form})
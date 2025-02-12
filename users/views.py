from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm
from django.shortcuts import HttpResponseRedirect


# Create your views here.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = RegisterForm()
    else:
        # Process completed form.
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return redirect('blog:base')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_user(request):
    print('Logout request reached view in users')
    logout(request)
    return redirect('/')


# def login(request, user):
#     """Log in a user."""

#     if request.method == 'POST':
#         # Display blank login form.
#         form = LoginForm()
        
#     else:
#         # Process completed form.
#         form = LoginForm(data=request.POST)

#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('blog:base')
    
#     # Display a blank or invalid form.
#     context = {'form':form}
#     return render(request, '/users/login.html')


def submit_login(request):
    print('submit login called')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print('Form pre valid check')


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
        
        # Below is used for debugging form errors
        # else:
        #     # print errors 
        #     print('form not valid', form.errors)

    else:
        print('else in form called')
        form = LoginForm()


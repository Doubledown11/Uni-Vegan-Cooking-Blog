from django import forms
from django.forms import ModelForm, DateInput

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User 
from .models import ProfilePicture, Enquiry



#  A form for the input required for the commenting functionality


# class RegisterForm(UserCreationForm):
#     email = forms.CharField(required=True)
    
#     class Meta:   
#         Model = User
#         Fields = ['username', 'email', 'password1', 'password2']




class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    # print('data in form', UserCreationForm)
    # print('email in forms', email)

    
    class Meta:
        model = User
        fields = ['username','password1', 'email' ]# 'password2']
        labels = {'username' : 'Enter Username', 'password1' : 'Enter Password', 'email' : 'Enter Email'} # 'password2' : 'Re-Enter Password'}
    

#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
		
#         print('self\n\n', self.data)
#         print('\n\n\n')


#         user.username = self.cleaned_data['username']
#         user.email = self.cleaned_data['email']
#         user.password = self.cleaned_data['password1']
#         print('User.Password', user.password)
#         print('\n\n\n')
#         user.set_password(user.password)

#         if commit:
#             user.save()
                  
#         return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username' : 'Enter Username', 'password' : 'Enter Password'}
         


class UploadPhotoForm(forms.ModelForm):
    """
    Form that allows users to upload profile pictures.
    """

    class Meta:
        model = ProfilePicture 
        fields = ['profile_picture']



class UpdateUserForm(forms.ModelForm):
    """
    We use modelForm which allows us to create forms which interact with 
    existing models inside of the database.
    """
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    

    class Meta:
        model = User
        fields = ['username', 'email']





class ContactForm(forms.ModelForm):
    fname = forms.CharField(max_length=50) #widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your First Name"})),
    lname = forms.CharField(max_length=50) # widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Last Name"})),
    email = forms.CharField(max_length=50) # widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Email"})),
    message = forms.CharField(max_length=500) # widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Message Here"}))
    select = forms.CharField(max_length=25) #required=True)

    class Meta:
        model = Enquiry
        fields = ['fname', 'lname', 'email', 'message', 'select']
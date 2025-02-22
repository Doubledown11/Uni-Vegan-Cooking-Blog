from django.db import models

from django.contrib.auth.models import User



# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #username = models.CharField(primary_key=True, max_length=25, unique=True)
    email = models.EmailField(null=False)
    #password = models.CharField(max_length=30, null=False)

    USERNAME_FIELD = 'username'
    #SET_PASSWORD = password
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user.username



class ProfilePicture(models.Model):
    """
    Models used to hold image upload data.
    """

    profile_picture = models.ImageField(upload_to='media/profile_pics/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    


class User(models.Model): 
    """
    entity for the various users of the system
    """
    id = models.AutoField(primary_key=True, unique=True)
    Fname = models.CharField(max_length=20, null = False)
    Lname = models.CharField(max_length=20, null=False)  





class Enquiry(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    message = models.CharField(max_length=500)
    select = models.CharField(max_length=100)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return f'{self.enquire_email}' 

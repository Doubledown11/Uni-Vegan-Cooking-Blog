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
    profile_picture = models.ImageField(default='blank_profile_pic.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    


class User(models.Model): 
    """
    entity for the various users of the system
    """
    id = models.AutoField(primary_key=True, unique=True)
    Fname = models.CharField(max_length=20, null = False)
    Lname = models.CharField(max_length=20, null=False)  



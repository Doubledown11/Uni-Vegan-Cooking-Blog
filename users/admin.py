from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, ProfilePicture, Enquiry

# Register your models here.
admin.site.register(ProfilePicture)
admin.site.register(Enquiry)

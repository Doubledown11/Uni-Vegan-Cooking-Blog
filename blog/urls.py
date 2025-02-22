# blog/urls.py
from django.contrib import admin 
from django.urls import path, include 
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path as url

app_name = 'blog'

urlpatterns = [
    # path('sign_in/', views.sign_in, name='sign_in'),

    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('base', views.base, name='base'),
    path('contact/', views.contact, name='contact'),

    path('responsive/', views.responsive),
    path('', views.blog_index_reponsive, name='blog_index_reponsive'),
    # path("category/<category>/", views.blog_category_responsive, name="blog_category_responsive"),
    # path("post/<int:pk>/", views.blog_detail_responsive, name="blog_detail_responsive"),


    path('send_enquiry/', views.send_enquiry, name='send_enquiry'),

]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
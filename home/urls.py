from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name= 'home'),
    # path("add", views.add, name= 'add'),
    path("about", views.about, name= 'about'),
    path("services", views.services, name= 'services'),
    path("Contact", views.Contact, name= 'Contact')

]
import imp
from django.shortcuts import render
#Listing Data from the database is common thing to do hence django is cool enough to create built in function called ListView to help us do so
from django.views.generic import ListView
from .models import MyPost

# Create your views here.
class HomePage(ListView):
    model= MyPost
    template_name= 'home.html'
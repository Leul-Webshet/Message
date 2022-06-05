import imp
from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import HomePage

urlpatterns=[
    path('',HomePage.as_view(),name='home')
]
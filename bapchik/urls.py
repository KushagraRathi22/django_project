from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('first-function/',first_function, name='first-function' ),

]

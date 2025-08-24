from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_function(request):
    return HttpResponse("hello")

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
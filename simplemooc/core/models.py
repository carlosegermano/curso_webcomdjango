from django.shortcuts import render
from django.db import models

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
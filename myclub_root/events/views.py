from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here.

def index(request):
    
    return HttpResponse("<h2>Myclub Event Calendar</h2>")

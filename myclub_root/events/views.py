from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here.

def index(request):
    t = date.today()
    month = date.strftime(t, '%b')
    year = t.year
    title = "MyClub Event Calendar - {} {}".format(month, year)
    return HttpResponse("<h2>{}</h2>".format(title))
    # return HttpResponse("<h2>Myclub Event Calendar</h2>")

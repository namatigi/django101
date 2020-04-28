from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Venue
from .forms import VenueForm


def index(request, year=date.today().year, month=date.today().month):
    """
    :param request:
    :param year:
    :param month:
    :return: title, calendar, page_title and announcement to the calendar_base.html template
    """
    # t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
        month = date.today().month
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - {} {}".format(month_name, year)
    # return HttpResponse("<h2>{}</h2>".format(title))
    # return HttpResponse("<h2>Myclub Event Calendar</h2>")
    cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse("<h2>{}</h2><p>{}</p>".format(title, cal))
    page_title = "MyClub Calendar"
    announcements = [
        {'date': '8-9-2020', 'announcement': "Club Registrations Open"},
        {'date': '5-5-2020', 'announcement': "Leonard Mangu elected President"}
    ]
    return render(request, 'events/calendar_base.html',
                  {'title': title, 'cal': cal, 'page_title': page_title, 'announcements': announcements})


def add_venue(request):
    """
    :param request:
    :return: form data and boolean data for submitted to the add_venue template.
    """
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return
        HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

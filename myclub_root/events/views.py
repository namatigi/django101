from django.shortcuts import render
# from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


# Create your views here.

def index(request, year=date.today().year, month=date.today().month):
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

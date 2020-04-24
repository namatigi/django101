from django.db import models


# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip/Post code', max_length=12)
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Events(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyclubUser)

    def __str__(self):
        return self.name
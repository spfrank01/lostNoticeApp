from django.db import models

# Create your models here.
class LostNoticeList(models.Model):
	title = models.CharField(max_length=200)
	name_item = models.CharField(max_length=200)
	time_lost = models.CharField(max_length=200)
	location_lost = models.CharField(max_length=200)
	detail = models.CharField(max_length=1000)
	your_name = models.CharField(max_length=200)
	your_email = models.CharField(max_length=200)
	found_it = models.BooleanField(default=False)
	time_submit = models.DateTimeField(null=True, blank=True)

class FindOwnerList(models.Model):
    title = models.CharField(max_length=200)
    name_item = models.CharField(max_length=200)
    time_found = models.CharField(max_length=200)
    location_found = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    your_name = models.CharField(max_length=200)
    your_email = models.CharField(max_length=200)
    found_owner = models.BooleanField(default=False)
    time_submit = models.DateTimeField(null=True, blank=True)

class userData(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	time_register = models.DateTimeField(null=True, blank=True)
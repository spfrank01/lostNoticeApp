from django.db import models

# Create your models here.
class SaveLostNoitce(models.Model):
    name_item = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    time_submit = models.DateTimeField('date published')
    your_name = models.CharField(max_length=200)
    your_email = models.CharField(max_length=200)
    your_telephone = models.CharField(max_length=200)

class userData(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	time_register = models.DateTimeField('date published')
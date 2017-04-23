from django.db import models

# Create your models here.
class SaveLostNoitce(models.Model):
    name_item = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000)
    time_submit = models.DateTimeField('date published')
    your_name = models.CharField(max_length=200)
    your_email = models.CharField(max_length=200)
    your_telephone = models.CharField(max_length=200)
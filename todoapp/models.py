from django.db import models


# Create your models here.
class todoapp(models.Model):
    notes = models.CharField(max_length=100)
    dates = models.DateTimeField()
    names = models.CharField(max_length=100)






from django.db import models


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.DateField()

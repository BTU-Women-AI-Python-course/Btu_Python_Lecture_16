from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    description = models.TextField()

from pickle import TRUE
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

class Task(models.Model):
    title = models.CharField(max_length=12)
    descrpition = models.CharField(max_length=12)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    dueDate = models.DateField()
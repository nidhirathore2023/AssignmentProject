from django import forms
from .models import User,Task

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','descrpition','assigned','dueDate']
    
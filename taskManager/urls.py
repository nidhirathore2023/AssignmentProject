from django.urls import path
from . import views

urlpatterns = [
    path('viewTaskAssigned/',views.viewTaskAssigned),
    path('createTask/',views.createTask)
]
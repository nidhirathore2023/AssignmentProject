from django.urls import path
from . import views

urlpatterns = [
    path('viewTaskAssigned/',views.viewTaskAssigned,name='viewTaskAssigned'),
    path('createTask/',views.createTask,name='createTask')
]
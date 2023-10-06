import json
from django.shortcuts import render
from .models import Task,User
from .forms import CreateTask
from django.contrib import messages
from .constants import USER
from django.core.mail import send_mail

def viewTaskAssigned(request):
    search_param = request.GET.get("search_param")
    search_value = request.GET.get("search_valueString")
    search_value_date = request.GET.get("search_valueDate")
    allTasks = Task.objects.all()
    if search_param=='assigned' and search_value!='' and search_value is not None:
        all = Task.objects.select_related().all()
        allTasks = all.filter(assigned__name__icontains=search_value)

    if search_param=='dueDate' and search_value_date!='' and search_value is not None:
        all = Task.objects.select_related().all()
        allTasks = all.filter(dueDate=search_value_date)
        print(allTasks)

    if search_param=='createdBy' and search_value!='' and search_value is not None:
        all = Task.objects.select_related().all()
        allTasks = all.filter(createdBy__icontains=search_value)
    return render(request,"viewTaskAssigned.html",{'tasks':allTasks})


def createTask(request):
    allUsers = User.objects.all()
    
    if request.method =='POST':
            request.POST = request.POST.copy()
            request.POST._mutable = True
            request.POST['createdBy'] = USER
            assigned = request.POST.getlist('assigned')
            form = CreateTask(request.POST or None)
            if form.is_valid():
                form.save()
                for user in assigned:
                    sendNotification(user,request)
                messages.success(request,"Task is created Successfully")
            else:
                messages.error(request,"Unable to create task")
    return render(request,"createTask.html",{'allUsers':allUsers})


# <-- Send Notifications -->

def sendNotification(assigned,request):
    userInstance = User.objects.filter(id=assigned)
    user = userInstance[0]
    # send_mail(
    # "Task Assigned",
    # "Task Assigned to you",
    # "nidhirathore2023@gamil.com",
    # [user.email],
    # fail_silently=False,
    # )
    # print(user.name)
    messages.success(request,"Email is send to - "+user.name)
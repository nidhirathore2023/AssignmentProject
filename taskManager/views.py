from django.shortcuts import render
from .models import Task,User
from .forms import CreateTask
from django.contrib import messages

def viewTaskAssigned(request):
    search_param = request.GET.get("search_param")
    search_value = request.GET.get("search_value")
    allTasks = Task.objects.all()

    if search_param=='assigned' and search_value!='' and search_value is not None:
        all = Task.objects.select_related().all()
        allTasks= all.filter(assigned__name__icontains=search_value)

    if search_param=='dueDate' and search_value!='' and search_value is not None:
        all = Task.objects.select_related().all()
        allTasks= all.filter(dueDate__icontains=search_value)

    if search_param=='createdBy' and search_value!='' and search_value is not None:
        all = Task.objects.select_related().all()
        allTasks= all.filter(assigned__name__icontains=search_value)
    return render(request,"viewTaskAssigned.html",{'tasks':allTasks})


def createTask(request):
    allUsers = User.objects.all()
    if request.method =='POST':
            form = CreateTask(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request,"Task is created Successfully")
            else:
                messages.error(request,"Unable to create task")
    return render(request,"createTask.html",{'allUsers':allUsers})

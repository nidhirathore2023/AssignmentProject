from django.shortcuts import render

# Create your views here.

def viewTaskAssigned(request):
    return render(request,"viewTaskAssigned.html",{})

def createTask(request):
    # all_memebers=Members.objects.all
    return render(request,"createTask.html",{})


# def sayhello(request):
#     all_memebers=Members.objects.all
#     return render(request,"hello.html",{'all':all_memebers})

# def join(request):
#     if request.method =='POST':
#         form = MemberForm(request.POST or None)
#         # print(form.fname)
#         if form.is_valid():
#             form.save()
#         messages.success(request,"Your Form is Submitted Successfully")
#             # return render(request,"hello.html",{})
#         return render(request,"join.html",{})
#     else:    
#         return render(request,"join.html",{})

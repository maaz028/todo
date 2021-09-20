from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages 
from .models import Task
# Create your views here.

def index(request):
    return render(request,'todoApp/home.html')

def addTask(request):
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        if len(id) > 0:
            data = Task.objects.get(id=id)
            data.title = title
            data.description = description
            data.date = date
            data.save()
            messages.success(request,'Data Updated Successfully!')
            return redirect('/tasks')
        else:
            
            data = Task(title=title,description=description,date=date)
            data.save()
            messages.success(request,'Data added Successfully')
            return redirect('/')

def tasks(request):
    data = Task.objects.all()
    params = {'tasks':data}
    return render(request,'todoApp/task.html',params)

def delete_task(request, id):
    data = Task.objects.get(id=id)
    data.delete()
    messages.success(request,'Task with id: '+str(id)+' has been deleted')
    return redirect('/tasks')

def update_task(request, id):
    data = Task.objects.get(id=id)
    params = {'update':data}
    return render(request,'todoApp/home.html',params)
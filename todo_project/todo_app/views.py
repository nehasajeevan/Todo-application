from django.shortcuts import render,redirect
from .models import Task

def index(request):
    if request.method=='POST':
        task_title=request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title)
        return redirect('/')
    tasks=Task.objects.all().order_by('-created_at')   
    return render(request,'index.html',{'tasks':tasks})

def toggle_task(request,id):
    task=Task.objects.get(id=id)
    task.completed=not task.completed
    task.save()
    return redirect('/')

def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def update_task(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        new_title=request.POST.get('title')
        if new_title:
            task.title=new_title
            task.save()
            return redirect('/')
    return render(request,'update.html',{'task':task})
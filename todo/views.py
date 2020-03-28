from django.shortcuts import render, redirect
from .models import *
from .forms import InputForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import *


# Create your views here.

def index(request):
    form = InputForm
    total_tasks = Task.objects.count()
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'total_tasks': total_tasks,
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/index.html', context)


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = InputForm(instance=task)

    if request.method == 'POST':
        form = InputForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'todo/edit_task.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)



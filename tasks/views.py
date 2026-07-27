from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def task_list(request):
    """Vista para listar todas las tareas"""
    tasks = Task.objects.all().order_by('-created_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/task_list.html', context)

def task_create(request):
    """Vista para crear una nueva tarea"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea creada exitosamente')
            return redirect('task_list')
    else:
        form = TaskForm()
    context = {
        'form': form,
        'title': 'Crear Nueva Tarea'
    }
    return render(request, 'tasks/task_form.html', context)

def task_detail(request, pk):
    """Vista para ver los detalles de una tarea"""
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context)

def task_update(request, pk):
    """Vista para actualizar una tarea"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada exitosamente')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    context = {
        'form': form,
        'title': f'Editar: {task.title}',
        'task': task,
    }
    return render(request, 'tasks/task_form.html', context)

def task_delete(request, pk):
    """Vista para eliminar una tarea"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarea eliminada exitosamente')
        return redirect('task_list')
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_confirm_delete.html', context)

def task_toggle_complete(request, pk):
    """Vista para marcar/desmarcar una tarea como completada"""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    messages.success(request, f'Tarea marcada como {'completada' if task.completed else 'pendiente'}')
    return redirect('task_list')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
from .models import Task
import json

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()  # ADD THIS
        from django.contrib.auth.models import User
        if User.objects.filter(username=email).exists():
            return render(request, 'tasks/register.html', {'error': 'A warrior with that email already exists.'})
        user = User.objects.create_user(username=email, email=email, password=email, first_name=name)  # CHANGE password=email + '_shinori' to password=password
        login(request, user)
        return redirect('dashboard')
    return render(request, 'tasks/register.html') 

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        # Use email as username
        from django.contrib.auth.models import User
        if User.objects.filter(username=email).exists():
            return render(request, 'tasks/register.html', {'error': 'A warrior with that email already exists.'})
        user = User.objects.create_user(username=email, email=email, password=email + '_shinori', first_name=name)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'tasks/register.html')


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    total = tasks.count()
    slayed = tasks.filter(is_slayed=True).count()
    remaining = tasks.filter(is_slayed=False).count()
    recent_tasks = tasks[:5]
    return render(request, 'tasks/dashboard.html', {
        'total': total,
        'slayed': slayed,
        'remaining': remaining,
        'recent_tasks': recent_tasks,
    })


@login_required
def my_tasks(request):
    filter_type = request.GET.get('filter', 'all')
    search_query = request.GET.get('q', '')

    tasks = Task.objects.filter(user=request.user)

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if filter_type == 'slayed':
        tasks = tasks.filter(is_slayed=True)
    elif filter_type == 'alive':
        tasks = tasks.filter(is_slayed=False)

    alive_tasks = tasks.filter(is_slayed=False)
    slayed_tasks = tasks.filter(is_slayed=True)

    return render(request, 'tasks/my_tasks.html', {
        'alive_tasks': alive_tasks,
        'slayed_tasks': slayed_tasks,
        'filter_type': filter_type,
        'search_query': search_query,
    })


@login_required
def priorities(request):
    tasks = Task.objects.filter(user=request.user, is_slayed=False)
    high = tasks.filter(priority='high')
    medium = tasks.filter(priority='medium')
    low = tasks.filter(priority='low')
    return render(request, 'tasks/priorities.html', {
        'high_tasks': high,
        'medium_tasks': medium,
        'low_tasks': low,
    })


@login_required
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '').strip()
        description = data.get('description', '')
        due_date = data.get('due_date') or None
        priority = data.get('priority', 'medium')

        if title:
            task = Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                due_date=due_date,
                priority=priority,
            )
            return JsonResponse({'success': True, 'task_id': task.id, 'title': task.title})
    return JsonResponse({'success': False})


@login_required
def slay_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_slayed = not task.is_slayed
    task.slayed_at = timezone.now() if task.is_slayed else None
    task.save()
    return JsonResponse({'success': True, 'is_slayed': task.is_slayed})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return JsonResponse({'success': True})


@login_required
def get_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return JsonResponse({
        'id': task.id,
        'title': task.title,
        'description': task.description or '',
        'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else '',
        'priority': task.priority,
        'is_slayed': task.is_slayed,
    })

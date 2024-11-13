from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Представление для редиректа на страницу логина
def redirect_to_login(request):
    # Если пользователь не авторизован, перенаправляем на страницу логина
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('task_list')

# Страница регистрации нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Войти в систему после регистрации
            return redirect('task_list')  # Перенаправляем на страницу списка задач
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Страница списка задач, доступная только для авторизованных пользователей
@login_required
def task_list(request):
    # Фильтруем задачи по текущему пользователю
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Страница создания задачи, доступная только для авторизованных пользователей
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Связываем задачу с текущим пользователем
            task.save()
            return redirect('task_list')  # Перенаправляем на страницу списка задач
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# Страница редактирования задачи, доступная только для авторизованных пользователей
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Фильтруем задачи по текущему пользователю
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Перенаправляем на страницу списка задач
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

# Страница удаления задачи, доступная только для авторизованных пользователей
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Фильтруем задачи по текущему пользователю
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Перенаправляем на страницу списка задач
    return render(request, 'tasks/delete_task.html', {'task': task})

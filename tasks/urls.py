from django.urls import path
from . import views

urlpatterns = [
    # Страница списка задач, доступная только для авторизованных пользователей
    path('', views.task_list, name='task_list'),
    
    # Страница создания задачи
    path('create/', views.create_task, name='create_task'),
    
    # Страница редактирования задачи
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    
    # Страница удаления задачи
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]

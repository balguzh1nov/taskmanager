from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views  # Импортируем представления из приложения tasks

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    
    # Перенаправляем с главной страницы на страницу логина
    path('', views.redirect_to_login, name='home'),
    
    # Включаем URL-ы приложения tasks
    path('tasks/', include('tasks.urls')),  # Подключаем URL-ы из приложения tasks
    
    # Страница логина (используем встроенный LoginView Django)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Страница регистрации
    path('register/', views.register, name='register'),
    
    # Страница выхода
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

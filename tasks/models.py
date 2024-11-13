from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    # Добавляем поле, которое ссылается на пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

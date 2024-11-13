# Клонируем репозиторий
- git clone https://github.com/balguzh1nov/taskmanager.git
- cd taskmanager

# Создаем и активируем виртуальное окружение
Если у тебя на Windows то вводишь эту команду: 
- venv\Scripts\activate

# Устанавливаем зависимости
- pip install -r requirements.txt

# Применяем миграции
- python manage.py makemigrations
- python manage.py migrate

# Создаем суперпользователя (по желанию)
- python manage.py createsuperuser

# Запускаем сервер
- python manage.py runserver




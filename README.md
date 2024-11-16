# Клонируем репозиторий
- git clone https://github.com/balguzh1nov/taskmanager.git
- cd taskmanager

# Создаем и активируем виртуальное окружение
Если у тебя на Windows то вводишь эту команду:
- python -m venv venv
- .\venv\Scripts\activate

# Устанавливаем зависимости
- pip install -r requirements.txt

# Применяем миграции
- python manage.py makemigrations
- python manage.py migrate

# Создаем админа
- python manage.py createsuperuser
python manage.py createsuperuser
Пример вот:
Username: admin
Email address: mail@mail.ru
Password: password
Password (again): password
This password is too common.
Bypass password validation and create user anyway? [y/N]: y

# Запускаем сервер
- python manage.py runserver

# Чтобы показать ты мог базу данных в терминале введи
- sqlite3 db.sqlite3
- .tables
- select * from tasks_task;




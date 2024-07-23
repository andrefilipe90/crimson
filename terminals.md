cd demo
django-admin startproject demo
python manage.py startapp crimson
python manage.py make migrations
python manage.py migrate
python manage.py runserver
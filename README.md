# sport
Для запуска проекта используйте команду <br>
```py manage.py runserver ```<br>
или <br>
```python manage.py runserver ```<br>
Так же установите фреймворки: <br>
```pip install django-rest-swagger```<br>
```pip install django-restframework-apiview```<br>
```pip install djangorestframework```<br>

База даных представлена sqlite3, чтобы изменить на postgresql раскомментируйте настройки 
связанные с postgresql и закомментируйте настройки sqlite3
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'sport',
    #     'USER': 'sport',
    #     'PASSWORD': 'sport',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # }
}
```

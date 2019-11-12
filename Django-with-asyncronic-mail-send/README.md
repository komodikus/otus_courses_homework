# ДЗ 9
Домашнее задание №9
Добавить асинхронную отправку почты
```
Загрузка данных в БД:
python manage.py loaddata db.json

Создание админа
python manage.py createsuperuser --username=admin

Установка зависимостей
pip install requirements.txt

Запуск python manage.py runserver
```  
Для начала запустите redis-server  

После в одном из терминалов необходимо запустить воркера  
```celery worker -A profile_user --loglevel=info --concurrency=4```  
Во втором терминале необходимо запустить менеджер который отправляет задачи по расписанию  
```celery -A profile_user beat --loglevel=info```  

### При регистрации пользователя, ему отсылается письмо для подтверждения регистрации  
### Каждые 2 часа проверяется нет ли урока в ближайшее время, если есть то отправляет письмо



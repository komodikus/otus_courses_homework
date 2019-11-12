# ДЗ 7
Домашнее задание №7
Сделать демо интернет-магазина на Django.
```
Загрузка данных в БД:
python manage.py loaddata db.json

Создание админа
python manage.py createsuperuser --username=admin

Запуск python manage.py runserver
```
### Информация о учителе `/teacher/api/teacher/<id>` – GET
Информация об учителе с  <ид>

### Информация о учителях `/teacher/api/teacher` – GET
Информация об учителях


### Информация о уроке `/lesson/api/lesson/<id>` – GET, DELETE
Информация об уроке с  <ид>

### Информация о уроках `/teacher/api/teacher` – GET, POST
Информация об уроках

### Информация о курcе `/course/api/course/<id>` – GET, DELETE
Информация о курсе с  <ид>

### Информация о курсах `/course/api/course` – GET, POST
Информация о курсах

### Информация о курcе `/profile/api/profile/<id>` – GET, DELETE
Информация о курсе с  <ид>

### Информация о курсах `/profile/api/profile` – GET, POST
Информация о курсах

### Регистрация пользователя на курс `/profile/register` – POST
{
"pk":1
}
pk - уникальный номер курса

### Аунтефикация пользователя на курс `/profile/login` – POST
{
"username":"korova",
"password":134566
}

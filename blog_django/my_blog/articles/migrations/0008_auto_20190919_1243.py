# Generated by Django 2.2.5 on 2019-09-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190919_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='theme',
            field=models.CharField(choices=[('work', 'Работка'), ('my_projects', 'Мои проекты'), ('travels', 'Путешествия'), ('mind', 'Мысли о всяком')], max_length=20),
        ),
    ]
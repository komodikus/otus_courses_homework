# Generated by Django 2.2.5 on 2019-09-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20190919_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='publication_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='theme',
            field=models.CharField(choices=[('work', 'Работка'), ('projects', 'Мои проекты'), ('travels', 'Путешествия'), ('mind', 'Мысли о всяком')], max_length=20),
        ),
    ]

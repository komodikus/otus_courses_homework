# Generated by Django 2.2.2 on 2019-06-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('description', models.CharField(max_length=150)),
                ('name_of_product', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('if_in_stock', models.BooleanField(default=True)),
                ('category_pets', models.IntegerField(choices=[(1, 'Котик'), (2, 'Собака')])),
                ('category_of_product', models.IntegerField(choices=[(1, 'Cухие корма'), (2, 'Наполнители'), (3, 'Консервы'), (4, 'Лотки'), (5, 'Совки'), (6, 'Игрушки'), (7, 'Домики'), (8, 'Переноски')])),
                ('stock_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

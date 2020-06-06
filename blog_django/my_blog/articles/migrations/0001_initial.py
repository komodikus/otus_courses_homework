# Generated by Django 2.2.5 on 2019-09-18 10:41

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('text_article', martor.models.MartorField()),
                ('publication_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
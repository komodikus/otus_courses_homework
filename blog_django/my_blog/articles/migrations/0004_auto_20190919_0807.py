# Generated by Django 2.2.5 on 2019-09-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190919_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='sub_title',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='theme',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
    ]

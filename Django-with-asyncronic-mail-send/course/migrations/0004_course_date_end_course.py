# Generated by Django 2.2.2 on 2019-06-21 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20190621_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_end_course',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

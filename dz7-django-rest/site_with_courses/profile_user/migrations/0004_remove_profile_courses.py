# Generated by Django 2.2.2 on 2019-06-23 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0003_profile_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='courses',
        ),
    ]

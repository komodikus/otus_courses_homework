# Generated by Django 2.2.2 on 2019-06-21 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_course_course_lenght'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teachers',
            new_name='teacher',
        ),
    ]

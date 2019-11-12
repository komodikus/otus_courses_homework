from django.contrib import admin
from .models import Lesson


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ['name', 'lesson_date', 'get_course']

    def get_course(self, obj):
        return obj.course.name
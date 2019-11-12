from django.contrib import admin

from .models import Course


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ['id','name', 'date_start_course', 'get_teachers', 'planned_duration']
    list_filter = ('name', 'date_start_course')

    def get_teachers(self, obj):
        return ', '.join(obj.teacher.values_list('name', flat=True))

    def planned_duration(self, obj):
        return obj.date_end_course - obj.date_start_course

    class Meta:
        fields = '__all__'

from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'name', 'description', 'date_start_course', 'date_end_course', 'teacher', 'price', 'studients', 'lessons'

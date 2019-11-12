from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer


def index_view(request):
    return HttpResponse('<h1>Hello Course View!</h1>')


class CourseView(APIView):

    def get(self, request):
        items = Course.objects.all()
        serializer = CourseSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        data = serializer.data
        course.delete()
        return Response(data)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Lesson
from .serializers import LessonSerializer


def index_view(request):
    return HttpResponse('<h1>Hello Lesson View!</h1>')


class LessonView(APIView):

    def get(self, request):
        items = Lesson.objects.all()
        serializer = LessonSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailView(APIView):

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

    def delete(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(lesson)
        data = serializer.data
        lesson.delete()
        return Response(data)
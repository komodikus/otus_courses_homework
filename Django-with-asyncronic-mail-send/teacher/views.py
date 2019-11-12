from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Teacher
from .serializers import TeacherSerializer


def index_view(request):
    return HttpResponse('<h1>Hello Lesson Teacher</h1>')


class TeacherView(APIView):

    def get(self, request):
        items = Teacher.objects.all()
        serializer = TeacherSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):

    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        data = serializer.data
        teacher.delete()
        return Response(data)
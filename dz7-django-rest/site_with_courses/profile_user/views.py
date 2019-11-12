from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from course.models import Course

from .models import Profile
from .serializers import ProfileSerializer


def index_view(request):
    return HttpResponse('<h1>Hello Profile</h1>')

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({'username': user.username,
                "token": user.auth_token.key,
                             'email': user.email})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = CsrfExemptSessionAuthentication,
    permission_classes = IsAuthenticated,

    def post(self, request):
        logout(request)
        return Response()


class ProfileView(APIView):
    # authentication_classes = ()

    def get(self, request):
        items = Profile.objects.all()
        serializer = ProfileSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(APIView):

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def delete(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        data = serializer.data
        profile.delete()
        return Response(data)


class RegisterOnCourseView(APIView):
    authentication_classes = CsrfExemptSessionAuthentication,
    # permission_classes = IsAuthenticated,

    def post(self, request):
        username = request.data.get("username")
        pk = request.data.get("pk")
        course = get_object_or_404(Course, pk=pk)
        user = request.user
        if user not in course.studients.all():
            user.courses.add(course)
            message = {"Success": "User {} successfully registered on course {}".format(user, course)}
            return Response(message, status=status.HTTP_201_CREATED)

        message = {"Not modified": "User {} is already registered on course {}".format(user, course)}
        return Response(message, status=status.HTTP_304_NOT_MODIFIED)
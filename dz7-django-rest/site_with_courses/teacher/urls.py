from django.urls import path
from . import views

app_name = 'Teacher'

urlpatterns = [
    path('', views.index_view),
    path('api/teacher/', views.TeacherView.as_view()),
    path('api/teacher/<int:pk>', views.TeacherDetailView.as_view()),
]

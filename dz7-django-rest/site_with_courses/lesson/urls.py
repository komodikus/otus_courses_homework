from django.urls import path
from . import views

app_name = 'Lesson'

urlpatterns = [
    path('', views.index_view),
    path('api/lesson/', views.LessonView.as_view()),
    path('api/course/<int:pk>', views.LessonDetailView.as_view()),
]
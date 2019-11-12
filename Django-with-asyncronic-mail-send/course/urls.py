from django.urls import path
from . import views

app_name = 'Course'

urlpatterns = [
    path('', views.index_view),
    path('api/course/', views.CourseView.as_view()),
    path('api/course/<int:pk>', views.CourseDetailView.as_view()),
]
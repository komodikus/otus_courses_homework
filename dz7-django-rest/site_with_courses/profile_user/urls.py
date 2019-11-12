from django.urls import path
from .views import LoginView, ProfileView, index_view, ProfileDetailView, RegisterOnCourseView

app_name = 'Profile'

urlpatterns = [
    path('', index_view),
    path('api/profile/', ProfileView.as_view()),
    path('api/profile/<int:pk>', ProfileDetailView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterOnCourseView.as_view())
]

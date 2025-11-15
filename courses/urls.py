from django.urls import path
from .views import CourseListView, CourseDetailView, LessonDetailView

app_name = "courses"

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('<slug:slug>/lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
]

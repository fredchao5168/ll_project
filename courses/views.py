from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Course, Lesson

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class LessonDetailView(DetailView):
    model = Lesson
    template_name = "courses/lesson_detail.html"
    context_object_name = "lesson"


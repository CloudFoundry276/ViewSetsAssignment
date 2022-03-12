from django.shortcuts import render
from vsApp.models import Course
from vsApp.serializers import CourseSerializer
from rest_framework import viewsets


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from .serializers import UserSerializer, TaskSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Task


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

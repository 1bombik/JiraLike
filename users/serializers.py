from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'task']


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'text', 'status', 'owner']

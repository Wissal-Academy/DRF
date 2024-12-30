from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    # assigned_to = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'assigned_to',
            'completed',
            'priority',
            'project'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField()
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'tasks'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

    def create(self, validate_data):
        return User.objects.create(
            username=validate_data["username"],
            email=validate_data["email"],
            password=validate_data["password"],
            last_name=validate_data["last_name"],
            first_name=validate_data["first_name"]
        )

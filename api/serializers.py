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
    owner = serializers.StringRelatedField()
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

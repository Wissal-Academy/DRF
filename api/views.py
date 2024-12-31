from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Task, Project
from .filters import ProjectFitler, TaskFitler
from .serializers import (
    TaskSerializer,
    ProjectSerializer,
    RegisterSerializer,
    ProjectMinSerializer,
    TaskMinSerializer
)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            return Response(
                {
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name
                    },
                    "refresh": str(refresh),
                    "access": str(access)
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# django-filter
class ProjectMinAPIView(ListAPIView):
    # Permissions
    permission_classes = [permissions.AllowAny]
    # Data
    queryset = Project.objects.all()
    serializer_class = ProjectMinSerializer
    # Filters
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFitler


class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskSearchAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    # Data
    queryset = Task.objects.all()
    serializer_class = TaskMinSerializer
    # Filters
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFitler

    # def get(self, request):
    #     # default queryset
    #     tasks = Task.objects.all()
    #     # Params
    #     title = request.query_params.get('title', None)
    #     completed = request.query_params.get('completed', None)

    #     if title:
    #         tasks = tasks.filter(title__icontains=title)
    #     if completed is not None:
    #         completed = completed.lower() in ['true', 1]
    #         tasks = tasks.filter(completed=completed)

    #     serializer = TaskMinSerializer(tasks, many=True)
    #     return Response(serializer.data)


# TODO:  FIX search view
class TaskSearch2APIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    # Data
    queryset = Task.objects.all()
    serializer_class = TaskMinSerializer
    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title']

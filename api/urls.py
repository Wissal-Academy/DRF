from django.urls import path

from .views import (
    ProjectDetailView,
    ProjectMinAPIView,
    ProjectListCreateView,
    TaskListCreateView,
    TaskDetailView,
    TaskSearchAPIView,
    # REGISTER
    RegisterView
)

# MAIN URL = project/
urlpatterns = [
    # LIST + CREATE A PROJECT
    path('', ProjectListCreateView.as_view()),
    # LIST + Search for Project
    path('min/', ProjectMinAPIView.as_view()),
    # DETAIL + UPDATE + DELETE A PROJECT
    path('detail/<pk>', ProjectDetailView.as_view()),
    # LIST + CREATE A Task
    path('task', TaskListCreateView.as_view()),
    # DETAIL + UPDATE + DELETE A Task
    path('task/detail/<pk>', TaskDetailView.as_view()),
    # Search API VIEW FOR TASK
    path('task/search', TaskSearchAPIView.as_view()),
    # PROJECT/register
    path('register', RegisterView.as_view())
]

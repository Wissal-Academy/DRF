from django.urls import path

from .views import (
    ProjectDetailView,
    ProjectListCreateView,
    TaskListCreateView,
    TaskDetailView,
    # REGISTER
    RegisterView
)

# MAIN URL = project/
urlpatterns = [
    # LIST + CREATE A PROJECT
    path('', ProjectListCreateView.as_view()),
    # DETAIL + UPDATE + DELETE A PROJECT
    path('detail/<pk>', ProjectDetailView.as_view()),
    # LIST + CREATE A Task
    path('task', TaskListCreateView.as_view()),
    # DETAIL + UPDATE + DELETE A Task
    path('task/detail/<pk>', TaskDetailView.as_view()),
    # PROJECT/register
    path('register', RegisterView.as_view())
]

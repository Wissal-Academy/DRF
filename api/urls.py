from django.urls import path

from .views import ProjectDetailView, ProjectListCreateView

urlpatterns = [
    path('', ProjectListCreateView.as_view()),
    path('detail/<pk>', ProjectDetailView.as_view())
]

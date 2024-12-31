import django_filters
from .models import Project, Task


class ProjectFitler(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Project
        fields = ['name']


class TaskFitler(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    completed = django_filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

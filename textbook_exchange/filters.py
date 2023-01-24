import django_filters

from .models import Book, Department

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'ISBN': ['icontains'],
            'author': ['icontains'],
            'price': ['icontains'],
            'instructor': ['icontains'],
            'course': ['icontains'],
        }

class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            'subject': ['icontains'],
        }
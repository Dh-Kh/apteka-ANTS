from django_filters import rest_framework as filters
from .models import EmployeeModel

class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = EmployeeModel
        fields = {
            'full_name': ['icontains'],
            'position': ['exact'],
            'joined': ['exact', 'gte', 'lte'],
            'email': ['icontains'],
        }
        
from django_filters import rest_framework as filters
from .models import EmployeeModel

class EmployeeFilter(filters.FilterSet):
    
    full_name = filters.CharFilter(field_name="full_name", lookup_expr="icontains")
    position = filters.NumberFilter(field_name="position")
    joined = filters.DateFromToRangeFilter(field_name="joined")
    email = filters.CharFilter(field_name="email" ,lookup_expr="icontains")
    
    class Meta:
        model = EmployeeModel
        fields = ['full_name', 'position',
                  'joined', 'email',]
        
        
        
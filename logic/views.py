from django.views.generic import (ListView, CreateView ,DetailView,
                                  UpdateView, DeleteView)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse
from .models import EmployeeModel
from .forms import CustomUserCreationForm, EmployeeForm

#need to implement lazy loading

class SortEmployers(ListView):
    model = EmployeeModel
    template_name = ""
    context_object_name = "queryset"
    paginate_by = 100
    def get_queryset(self):
        order_type = self.kwargs.get("type")
        return EmployeeModel.objects.order_by(order_type)
    
class FindEmployer(DetailView):
    model = EmployeeModel
    template_name = ""
    context_object_name = "object"
    
    def get_object(self):
        pass    
    

    

    

    

    
        
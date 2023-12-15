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

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "logic/register.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm
    success_message = "Your profile was created successfully"
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid data provided')
        return self.render_to_response(self.get_context_data(form=form))
    
class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "logic/login.html"
    
    def get_success_url(self):
        return reverse_lazy('sort') 
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid data provided')
        return self.render_to_response(self.get_context_data(form=form))
    
class SortEmployeeView(ListView):
    template_name = "logic/sort.html"
    model = EmployeeModel

    def get_queryset(self):
        url_parameter = self.request.GET.get("sorted_by", "position")
        queryset = EmployeeModel.objects.all()
        if url_parameter != None:
            queryset = queryset.order_by(url_parameter)    
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context["sorted_queryset"] = queryset
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            sorted_queryset = [
            {'full_name': employee.full_name,
             'position': employee.position,
             'joined': employee.joined,
             'email': employee.email,
             'boss': employee.boss.full_name if employee.boss is not None else ""}
            for employee in context['sorted_queryset']]
            return JsonResponse(sorted_queryset, safe=False)
        return super().render_to_response(context, **response_kwargs)

    

class FilterEmployeeView(ListView):
    template_name = "logic/find.html"
    model = EmployeeModel
    ordering = ["id"]
    
    def get_queryset(self):
        url_parameter = self.request.GET.get("full_name", "")
        queryset = EmployeeModel.objects.filter(full_name__icontains=url_parameter)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context["model_filter"] = queryset
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            model_filter = [
            {'full_name': employee.full_name,
             'position': employee.position,
             'joined': employee.joined,
             'email': employee.email,
             'boss': employee.boss.full_name if employee.boss is not None else ""}
            for employee in context['model_filter']]
            return JsonResponse(model_filter, safe=False)
        return super().render_to_response(context, **response_kwargs)
    
class HierarchyEmployeeView(ListView):
    template_name = "logic/hierarchy.html"
    model = EmployeeModel
    
    def get_queryset(self):
        queryset = EmployeeModel.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        hierarchy_tree = [employee.hierarchy_tree() for employee in queryset]
        context["hierarchy_tree"] = hierarchy_tree
        return context
    
class CreateEmployeeView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = "login"
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = "logic/create.html"
    success_url = reverse_lazy("sort")

class DetailEmployeeView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = "login"
    model = EmployeeModel
    template_name = "logic/detail.html"

class UpdateEmployeeView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = "login"
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = "logic/update.html"
    success_url = reverse_lazy("sort")
    
class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = "login"
    model = EmployeeModel
    template_name = "logic/delete.html"
    success_url = reverse_lazy("sort")


    

    
        
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import EmployeeModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields["boss"] = forms.ModelChoiceField(queryset=EmployeeModel.objects.all())
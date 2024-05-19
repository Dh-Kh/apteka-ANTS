from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import EmployeeModel

class EmployeeAdmin(TreeAdmin):
    form = movenodeform_factory(EmployeeModel)

admin.site.register(EmployeeModel, EmployeeAdmin)
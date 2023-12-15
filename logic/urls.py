from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (SignUpView, CustomLoginView, SortEmployeeView,
                    FilterEmployeeView, HierarchyEmployeeView, CreateEmployeeView,
                    DetailEmployeeView, UpdateEmployeeView, DeleteEmployeeView)

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("sort/", SortEmployeeView.as_view(), name='sort'),
    path("find/", FilterEmployeeView.as_view(), name='find'),
    path("hierarchy/", HierarchyEmployeeView.as_view(), name='hierarchy'),
    path("create/", CreateEmployeeView.as_view(), name="create"),
    path("employee/<int:pk>/", DetailEmployeeView.as_view(), name="detail"),
    path("employee/<int:pk>/update/", UpdateEmployeeView.as_view(), name='update'),
    path("employee/<int:pk>/delete/", DeleteEmployeeView.as_view(), name='delete'),    
]
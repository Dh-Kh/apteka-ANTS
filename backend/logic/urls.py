from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SortEmployeeView, FilterEmployeeView, RegisterView,
                    LoginView, LogOutView, EmployeeViewSet, 
                    ReassignEmployeeView, DisplayUserView)

router = DefaultRouter()
router.register("employee/", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("sort/<str:field>/", SortEmployeeView.as_view(), name="sort"),
    path("filter/", FilterEmployeeView.as_view(), name="filter"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("reassign/<int:id>/", ReassignEmployeeView.as_view(), name="reassign"),
    path("display/", DisplayUserView.as_view(), name="display"),
    path("", include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SortEmployers

router = DefaultRouter()
router.register("sort/<str:type>/", SortEmployers)

urlpatterns = [
    path('', include(router.urls)),    
]
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                     UpdateAPIView, RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404
from .models import EmployeeModel
from .serializers import (EmployeeModelSerializer, UserSerializer, 
                          DisplayUserSerializer)
from .pagination import CustomPageNumberPagination
from .filters import EmployeeFilter


class SortEmployeeView(ListAPIView):
    lookup_url_kwarg = "field"
    serializer_class = EmployeeModelSerializer
    pagination_class = CustomPageNumberPagination
    def get_queryset(self):
        field = self.kwargs.get(self.lookup_url_kwarg)
        return EmployeeModel.objects.order_by(field)


class FilterEmployeeView(ListAPIView):
    serializer_class = EmployeeModelSerializer
    queryset = EmployeeModel.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    pagination_class = CustomPageNumberPagination
    
#merge filter and sort

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = None

        user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    
class LogOutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DisplayUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DisplayUserSerializer
    
    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)

    
class EmployeeViewSet(ModelViewSet):

    queryset = EmployeeModel.objects.all()
    
    serializer_class = EmployeeModelSerializer
    
    pagination_class = CustomPageNumberPagination
    
    permission_classes = [IsAuthenticated]
         
    @action(detail=True, methods=["patch"])
    def update_parent(self, request, pk=None):
        try:
            instance = get_object_or_404(self.queryset, pk=pk)
            parent = instance.get_parent()
            serializer = self.serializer_class(parent, data=request.data, partial=True)
            if serializer.is_valid():
                for field, value in serializer.validated_data.items():
                    if value is not None and value != "":
                        setattr(instance, field, value)
            parent.save()
            parent.check_demotion()
            return Response({'message': 'parent updated'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#maybe need to merge with EmployeeViewSet
    
class ReassignEmployeeView(UpdateAPIView):
    lookup_url_kwarg = "id"
    serializer_class = EmployeeModelSerializer
    
    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        return get_object_or_404(EmployeeModel, id=id)
    
    def get_previous_boss(self):
        previous_boss_id = self.request.GET.get("previous_boss")
        return get_object_or_404(EmployeeModel, id=previous_boss_id)
    
    def update(self, request, *args, **kwargs):
        
        employee = self.get_queryset()
        previous_boss = self.get_previous_boss()

        if not employee or not previous_boss:
            return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        previous_boss.redistribute(employee)
                
        return Response({'message': "childs reassigned"}, status=status.HTTP_200_OK)
        
        
        
            






    

    

    

    
        
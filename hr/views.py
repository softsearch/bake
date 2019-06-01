from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .permissions import IsOwnerOrAdmin





from hr.serializers import EmployeeSerializer
from hr.models import Employee


class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = Employee
        exclude = ['image']


class EmployeeList(generics.ListCreateAPIView):
    """
        * View a list of all the employee
        * Only admin users are able to access this view.
        * Auth required
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer
    # filter_backends = (rest_filters.SearchFilter,)

 
    filterset_class = EmployeeFilter


class EmployeeUpdateRetrieveDelete(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    permission_classes = (IsOwnerOrAdmin, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 


        

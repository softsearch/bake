from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from hr.serializers import EmployeeSerializer
from hr.models import Employee




class EmployeeList(generics.ListCreateAPIView):
    """
        * View a list of all the employee
        * Only admin users are able to access this view.
        * Auth required
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer
   



        

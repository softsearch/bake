from django.urls import path, include
from hr.views import EmployeeList

urlpatterns = [
  path('employee/', EmployeeList.as_view())
]

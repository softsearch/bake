from django.urls import path, include
from hr.views import EmployeeList, EmployeeUpdateRetrieveDelete

urlpatterns = [
  path('employee/', EmployeeList.as_view(), name="employees"),
  path('employee/<int:pk>', EmployeeUpdateRetrieveDelete.as_view())
]

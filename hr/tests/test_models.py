from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Employee, Children

class EmployeeTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username = "Test User", password="Password")
        self.employee = Employee.objects.create(user = user)

    def test_create_an_employee_from_user(self):
        employee = Employee.objects.first()
        self.assertEqual(employee.user, get_user_model().objects.first())

    
    def test_create_an_employee_can_have_children(self):
        self.employee.children.create(name="Text")
        self.assertEqual(len(self.employee.children.all()), 1)
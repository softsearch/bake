from django.db import models
from datetime import datetime, timezone
from django.contrib.auth import get_user_model
from datetime import date
import hashlib

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    
class Employee(models.Model):

    GENDER_CHOICES = (
        ("F", 'Female'),
        ("M", 'Male'),
        ("N", 'Dont say'),
        ("O", 'Other'),
    )

    MARITAL_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    )

    EDUCATION_LEVEL = (
        ('primary', 'Primary School'),
        ('secondary', 'Secondary School')
    )


    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    kra_pin = models.CharField(max_length=64, blank=True, null=True)
    bank_account = models.CharField(max_length=64, blank=True, null=True)
    nhif = models.CharField(max_length=64, blank=True, null=True)
    nssf = models.CharField(max_length=64, blank=True, null=True)
    job_title = models.CharField(max_length=128,blank=True, null=True)
    identification_id  = models.CharField(max_length=64, blank=True, null=True) 
    gender = models.CharField(
                max_length=2,
                default='F',
                choices=GENDER_CHOICES,
        )
    active = models.BooleanField(default=True)
    marital = models.CharField(
                max_length=64,
                default='single',
                choices=MARITAL_CHOICES,
        ) 
    

    spouse_complete_name = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    spouse_birthdate = models.DateField(blank=True, null=True) 
    number_of_children = models.IntegerField(blank=True, null=True)
    place_of_birth = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    birthday = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    country_of_birth = models.CharField(
        max_length=128,
        null=True,
        blank=True
    ) 

    # notes about employee
    notes = models.TextField(blank=True, null=True)
    permit_no = models.CharField(max_length=64, blank=True, null=True)
    visa_no =  models.CharField(max_length=64, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    education_level = models.CharField(
        max_length=64,
        default="secondary",
        choices=EDUCATION_LEVEL
    ) 
    study_field = models.CharField(max_length=64, blank=True, null=True)
    study_school = models.CharField(max_length=64, blank=True, null=True)

    work_phone = models.CharField(
        max_length=64,
        blank=True
    )

    phone = models.CharField(
        max_length=64,
        blank=True
    )

    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
    emergency_contact = models.CharField(
        max_length=64,
        blank=True
    )

    emergency_phone = models.CharField(
        max_length=64,
        blank=True,
        null=True
    ) 

    google_drive_link = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )

    image = models.ImageField(upload_to=user_directory_path, default="https://www.gravatar.com/avatar/")

    manager = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    

    
    def get_default_image(self):
        return f'https://www.gravatar.com/avatar/{hashlib.md5(self.user.email.lower()).hexdigest()}'



    def __str__(self):
        return self.user.username


    def __repr__(self):
        return self.user.username



class LeaveType(models.Model):
    UNITS = (
        ('day', 'Day'), ('hour', 'Hours')
    )
    name = models.CharField(max_length=64)
    unpaid = models.BooleanField(default=True, help_text="Is Unpaid")
    request_unit = models.CharField(
        max_length=32,
        default="day",
        help_text="Take Leaves in"
    )

    valid = models.BooleanField(default=True)

    

class Leave(models.Model):
    # TODO create a better leave module
    employee = models.ForeignKey(Employee,  on_delete=models.CASCADE, related_name='employee_l')
    supervisor =  models.ForeignKey(Employee,  on_delete=models.CASCADE, related_name='supervisor')
    status = models.CharField(max_length=64, blank=True)
    days = models.DecimalField(max_digits=4, decimal_places=1)
    start_date = models.DateField()
    end_time = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return self.status





class Next_of_keen(models.Model):
    GENDER_CHOICES = (
        ("F", 'Female'),
        ("M", 'Male'),
        ("N", 'Dont say'),
        ("O", 'Other'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True)
    relationship = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=2,
                            default='F',
                            choices=GENDER_CHOICES
            )
    phone_number =models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=64, blank=True)


    def __str__(self):
        return self.name + ' ' + str(self.employee)


class Children(models.Model):
    GENDER_CHOICES = (
        ("F", 'Female'),
        ("M", 'Male'),
        ("N", "Don't say"),
        ("O", 'Other'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=2,
                            default='F',
                            choices=GENDER_CHOICES
            )
    phone_number =models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=64, blank=True)


class Attendance(models.Model):
    employee = models.ForeignKey(Employee,  on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)
    date = models.DateField(default=date.today)
    
    #  TODO check valid check in and checkout

    @property
    def worked_hours(self):
        if self.check_out:
            delta = self.check_out - self.check_in
            return delta.total_seconds() / 3600.0
        
        return (datetime.now(timezone.utc) - self.check_in).total_seconds() / 3600.0 
        



    def __str__(self):
        return f'{str(self.employee)} - {str(self.date)}' 

class Department(models.Model):
    name = models.CharField(
        max_length=64
    )
    complete_name = models.CharField(max_length=64)
    active = models.BooleanField(default=True) 
    manager_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="manager_department")
    parent = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='child')
    note = models.TextField()

# class Employment(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
#     salary = models.DecimalField(max_digits=6, decimal_places=2)
#     start_date =  models.DateField(default=date.today)
#     end_date = models.DateField()
#     supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='supervisor')
#     job_title = models.CharField(max_length=255, blank=True)
    
    


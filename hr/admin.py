from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from .models import Employee, Next_of_keen, Leave, Attendance, Children

class Next_of_keenAdminInline(admin.TabularInline):
    model = Next_of_keen

class ChildrenAdminInline(admin.TabularInline):
    model = Children

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    inlines= [
        Next_of_keenAdminInline,
        ChildrenAdminInline
    ]



class Next_of_keenAdmin(admin.ModelAdmin):
    model = Next_of_keen



class LeaveAdmin(admin.ModelAdmin):
    model =  Leave

class AttendanceAdmin(admin.ModelAdmin):
    model = Attendance
    list_display = ['employee','date','check_in','check_out', 'worked_hours']
    fields = ('employee','date','check_in','check_out')
    

# admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Leave, LeaveAdmin)
admin.site.register(Next_of_keen, Next_of_keenAdmin)
admin.site.register(Attendance, AttendanceAdmin)


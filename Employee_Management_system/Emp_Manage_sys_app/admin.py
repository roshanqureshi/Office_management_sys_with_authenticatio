
from django.contrib import admin

from Emp_Manage_sys_app.models import Department, Employee, Role

# Register your models here.
@admin.register(Employee)
@admin.register(Department)
@admin.register(Role)

class EmployeeAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


class RoleAdmin(admin.ModelAdmin):
    pass
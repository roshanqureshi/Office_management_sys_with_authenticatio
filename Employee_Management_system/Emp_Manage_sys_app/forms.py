from dataclasses import fields
import imp
from pydoc import classname
from django import forms

from Emp_Manage_sys_app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        
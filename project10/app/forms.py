from django import forms
from app.models import Employee
from django.shortcuts import redirect, render
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"



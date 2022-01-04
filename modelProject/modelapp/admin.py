from django.contrib import admin
from .models import Employee
# Register your models here.
# admin.site.register(Employee)

#  To Display Data in admin Interface in Browser:


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']


admin.site.register(Employee, EmployeeAdmin)

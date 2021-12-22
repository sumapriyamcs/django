from django.contrib import admin
# Register your models here.
from .models import Employee
# Register your models here.
#register your models here
@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display=("eid","ename","econtact")
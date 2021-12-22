from django.contrib import admin

# Register your models here.
#from django.contrib import admin

# Register your models here.
from .models import Student
# Register your models here.
#register your models here
@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name")

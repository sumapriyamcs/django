'''
1.Django Admin:

Django provides an admin site to allow CRUD (Create Read Update Delete)
operations on registered app model.

It is a built-in feature of Django that automatically generates interface for models.

We can see the url entry for admin in urls.py file, it is implicit and generated while creating a new project.

urlpatterns = [
    path('admin/', admin.site.urls),
]

It can be easily accessed by after login from the admin panel,
lets run the server python3 manage.py runserver and access it through the localhost:8000/admin.
A login form will be displayed
To login, first create admin (super user) user and provide password
once Super user is created successfully, now login.
It shows a home page after successfully login
It is an admin dashboard that provides facilities like: creating groups and users.
It also used to manage the models.

2.Register Django Model:

To register model in admin.py file. Use the admin.site.register() method and pass
the Model name. See the example.

// admin.py

from django.contrib import admin
from myapp.models import Employee
admin.site.register(Employee) # Employee is registered

Login again and see, it has employee object.

It provides auto generated interface to create new model object. Like, if i
click on add, it renders a form with all the attributes provided in the model class.

For example, our model class contains the following code.

// models.py

from django.db import models
class Employee(models.Model):
    eid     = models.CharField(max_length=20)
    ename   = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"

The auto generated form will be based on the model. We don't need to
write HTML to create form.
Lets add an employee by providing details and click on save button.
After saving, record is stored into the database table
Using this admin dashboard, we can update and delete record also.
'''

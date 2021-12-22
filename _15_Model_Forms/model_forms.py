'''
1.Django Model Form:

It is a class which is used to create an HTML form by using the Model.
It is an efficient way to create a form without writing HTML code.

Django automatically does it for us to reduce the application development time.
For example, suppose we have a model containing various fields, we don't need to
repeat the fields in the form file.

For this reason, Django provides a helper class which allows us to create
a Form class from a Django model.

2.Django ModelForm Example:

First, create a model that contains fields name and other metadata.
It can be used to create a table in database and dynamic HTML form.

// model.py

from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=30)
    class Meta:
        db_table = "student"

This file contains a class that inherits ModelForm and mention the model name
for which HTML form is created.


// form.py

from django import forms
from myapp.models import Student

class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
Write a view function to load the ModelForm from form.py.

//views.py

from django.shortcuts import render
from myapp.form import StuForm

def index(request):
    stu = EmpForm()
    return render(request,"index.html",{'form':stu})
//urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
And finally, create a index.html file that contains the following code.

3.Run Server:

Run the server by using python manage.py runserver command.
After that access the template by localhost:8000/index URL
Well, an HTML form is created automatically. This is a feature of Django.


'''
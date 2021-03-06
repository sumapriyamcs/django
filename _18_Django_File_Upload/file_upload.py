'''
1.Django File Upload:

File upload to the server using Django is a very easy task.
Django provides built-in library and methods that help to upload a file to the server.

The forms.FileField() method is used to create a file input and submit the
file to the server. While working with files, make sure the HTML form
tag contains enctype="multipart/form-data" property.

Let's see an example of uploading a file to the server.

This example contains the following files.

Template (index.html)

It will create an HTML form which contains a file input component.

<body>
<form method="POST" class="post-form" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
</form>
</body>

#Form (forms.py)

from django import forms
class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 10)
    email     = forms.EmailField(label="Enter Email")
    file      = forms.FileField() # for creating file input

#View (views.py)

Here, one extra parameter request.FILES is required in the constructor.
This argument contains the uploaded file instance.

from django.shortcuts import render
from django.http import HttpResponse
from myapp.functions.functions import handle_uploaded_file
from myapp.form import StudentForm
def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})

#Specify URL (urls.py)

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]

2.Upload Script (functions.py):

This function is used to read the uploaded file and store at provided location.
Put this code into the functions.py file. But first create this file into the project.

def handle_uploaded_file(f):
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
Now, create a directory upload to store the uploaded file.
Initially, this directory is empty. so, let's upload a file to it and later
on it will contain the uploaded file.

3.Start Server:
python manage.py runserver

Submit this form and see the upload folder. Now, it contains the uploaded file.

'''
'''
1.Django Class Based Generic Views:

Django is the most popular web framework of Python, which is used in rapid
web application development. It provides a built-in interface that makes it
easy to work with it. It is also known as the Batteries included framework
because it offers built-in facilities for each operation.

Most of us may be already familiar with the function-based views and know how
to handle the requests using the function-based view. If you don't familiar with
them, visit our Django tutorials.

In this tutorial, we will introduce the Class-Based Generic views. These are
the advanced set of Built-in views and are used to implement the selective
CRUD (create, retrieve, update, and delete) operations. Using Class-Based
views, we can easily handle the GET, POST requests for a view.

These do not substitute for a function-based view but provide some additional
facilities over the function-based view.

2.Let's have a brief overview of function-based views and class-based views.

Function-Based Views

Function-based views are beginner-friendly; beginners can easily understand them.
It is quite easy to understand in comparison to class-based views.

1.It is easy to understand and easy to use.
2.It provides the explicit code flow.
3.Straightforward usage of decorators.
But function-based view can't be extended and also leads to code redundancy.

Class-Based Views

Class-based views can be used in place of function-based views. All the operations
handle using Python objects instead of functions. They provide some excellent
example over the function-based views. Class-based views can implement CRUD
operation in easy manner.

1.It follows the DRY convention of Django.
2.We can extend class-based views and can add more functionality according to
a requirement using Mixin.
3.It allows to inherit another class, can be modified for various use cases.
But these are complex to understand and hard to read. It has implicit code flow.

3.Perform CRUD (Create, Retrieve, Update, Delete) Using Class Based Views:

We will demonstrate how to create the basic crud application using the class based view.

We will create the project name Hello which includes an app named sampleapp

In the application, we will create an Employee model in the model.py file.

Example -

from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

And then we run the following command.

python manage.py makemigrations
python manage.py migrate

Now, we will create the Django ModelForm for this model in the form.py file.
It will use to display the form to the template.

forms.py

from django.forms import fields
from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):

    class Meta:
        # To specify the model to be used to create form
        model = Employee
        # It includes all the fields of model
        fields = '__all__'

4.Implementing Class Based Views:

The function-based view returns the different HTTP request methods with
different class instance method.

from django.http import HttpResponse
def function_view(request):
    if request.method == 'GET':
        # View logic will place here
        return HttpResponse('response')

If we implement the class based view, it would look as follows.

from django.http import HttpResponse
from django.views import View
class NewView(View):
    def get(self, request):
        # View logic will place here
        return HttpResponse('response')

To handle class based views, we need to use the as_view() in the urls.py file.

# urls.py

from django.urls import path
from myapp.views import NewView

urlpatterns = [
    path('about/', NewView.as_view()),
]

5.CreateView:

CreateView implements the view to create an instance of a table in the database.
This view automatically does everything for creating an instance. We only need
to specify the model name to create a view and its fields. The class-based create
view will search for employee_form.html.

Note - The employee_form.html file should be included in the
template/app_name/employee_form.html. In our case, the file location is
template/sampleapp/employee_form.html.

View.py

from .models import Employee
from .forms import EmployeeForm
from django.views.generic.edit import CreateView

class EmployeeCreate(CreateView):
    model = Employee

    fields = '__all__'

urls.py

from django.urls import path
from .views import EmployeeCreate

urlpatterns = [
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate')
]
Now we run the server on local host.
we got the form where we can create an employee.
As we can see in the admin panel, the employee has been created in database.

7.Retrieve View:

There are two kinds of retrieve view - ListView and DetailView. We will use
the ListView which refers to a view to display multiple instances of a table
in database. We only need to specify the model name which apply ListView, Class
based ListView will automatically do the job for us. To retrieve the data, we
need to create the app_name/modelname_list.html file.

views.py

from django.views.generic.list import ListView

class EmployeeRetrieve(ListView):
    model = Employee

url.py

from django.urls import path
from .views import EmployeeCreate, EmployeeRetrieve

urlpatterns = [
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve')
]

#sampleapp/template/employee_list.html:

{% extends 'base.html' %}

{% block content %}
    <ul class="nav flex-column">
        <!-- Iterate over object_list -->
        {% for object in object_list %}
        <!-- Display Objects -->
        <li class="nav-item">First Name: {{ object.first_name }}</li>
        <li class="nav-item">Last Name: {{ object.last_name }}</li>
        <li class="nav-item">Mobile: {{ object.mobile }}</li>
        <li class="nav-item"> Email: {{ object.email }}</li>

        <hr/>
        <!-- If object_list is empty -->
        {% empty %}
        <li class="nav-item">No objects Find</li>
        {% endfor %}
    </ul>

{% endblock content %}

Now, we run the localhost server and send the request to get the data.

9.DetailView:

DetailView is different from ListView as it displays the one instance of a table
in the database. Django automatically assigns a primary key for each entry,
and we need to specify the <pk> in the request. DetailView will automatically
perform everything. The implementation of DetailView is the same as the ListView,
and we need to create modelname_detail.html.

Let's understand the following implementation of DetailView.

View.py

from django.views.generic.detail import DetailView

class EmployeeDetail(DetailView):
    model = Employee

url.py

from django.urls import path
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve

urlpatterns = [
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('retrieve/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail')
]

#sampleapp/template/employee_detail.html

{% extends 'base.html' %}

{% block content %}

    <h1>{{ object.first_name }} {{object.last_name}}</h1>

    <p>{{ object.email }}</p>
    <p>{{ object.mobile }}</p>

{% endblock content %}

We created a new employee and it assigned 2 as primary key. Running the server
and provide the request with primary key.

10.UpdateView:

UpdateView allows to update the particular instance of the table from the
database with some more details. This view is used to alter the entries in the
database. For example, we want to change the user's first last name. We need
to specify the model name, and it will do everything automatically. Let's see
the following implementation of UpdateView.

We have already created the employee_form.html file in the template. In our
case, it is D:\python_project\Myfirstdjangoproject\hello\template\employee_form.html>

View.py

from django.views.generic.edit import UpdateView
class EmployeeUpdate(UpdateView):
    model = Employee

url.py

from django.urls import path
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name = 'EmployeeDelete')

]
We have updated the last name of object. The updated value will be added
to the database automatically.
We have updated the last name of object. The updated value will be added to the database automatically.

11.DeleteView:

DeleteView allows to deletion of the instance of a table from the database.
It is used to delete the entries in the database.

We just need to specify model name and it will do everything automatically.
Let's see the following implementation of UpdateView.

view.py

from django.views.generic.edit DeleteView

class EmployeeDelete(DeleteView):
    model = Employee

    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/'

Now, we create the URL path to map the view.

url.py

from django.urls import path
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('<pk>/update/', EmployeeUpdate, name = 'EmployeeUpdate'),
    path('<pk>/delete/', EmployeeDelete, name = 'EmployeeDelete')

]

Now, we create the template/sampleapp/employee_confirm_delete.html.

{% extends 'base.html' %}

{% block content %}

    <form method="post">
{% csrf_token %}

    <p>Are you sure you want to delete "{{ object }}"?</p>

    <input type="submit" value="Confirm">
</form>

{% endblock content %}

When we click on the confirm button, the object will be deleted and redirected to the homepage.

We have created the CRUD operations using the class

16.Code Below is the complete code of class based generic views.:

View.py

from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class EmployeeCreate(CreateView):
    model = Employee

    fields = '__all__'
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')

class EmployeeRetrieve(ListView):
    model = Employee
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')

class EmployeeDetail(DetailView):
    model = Employee
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('sampleapp: EmployeeRetrieve')

    # def get_success_url(self):



class EmployeeDelete(DeleteView):
    model = Employee
    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/'

Hello/urls.py

"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('sampleapp.urls'), namespace='sampleapp'))

]

sampleapp/url.py

from django.urls import path
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete

app_name = 'sampleapp'
urlpatterns = [
    path('', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name = 'EmployeeDelete')

]

template/base.html

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Register Page</title>
  </head>
  <body>
  <div class = 'col-md-8'>
     {% if messages %}
        <ul>
            {% for message in messages %}
              <div class = 'alert alert-{{message.tags}}'>
                {{ message }}
              </div>
              {% endfor %}
        </ul>
    {% endif %}
  </div>
  {% block content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


    {% endblock content %}
  </body>
</html>

template/sampleapp/employe_list

{% extends 'base.html' %}

{% block content %}

<table class="table table-borderless">
    <thead class="border-bottom font-weight-bold">
        <tr>
            <td>First Name</td>
            <td>Last Name</td>
            <td>Mobile</td>
            <td>Email</td>
                {% comment %} <a href="{% url 'EmployeeRetrieve' %}" class="btn btn-outline-success">
                    <i class="fas fa-plus"></i> Add New {% endcomment %}
                </a>
            </td>
        </tr>
    </thead>

    {% for object in object_list %}
        <!-- Display Objects -->
        <tr>
                <td>{{ object.first_name }}</td>
                <td> {{object.last_name }}</td>
                <td> {{object.mobile }}</td>
                <td>{{object.email }} </td>

            <td>
            <td><button><a href = '/{{object.pk}}/delete' class = 'class="btn text-secondary px-0'> Delete
            </a></button></td>

            <td><button><a href = '/{{object.pk}}/update' class = 'class="btn text-secondary px-0'> Update
            </a></button></td>
    {% endfor %}

</table>

template/sampleapp/employe_detail

{% extends 'base.html' %}

{% block content %}

    <h1>{{ object.first_name }} {{object.last_name}}</h1>

    <p>{{ object.email }}</p>
    <p>{{ object.mobile }}</p>

    <td><button><a href = '/{{object.pk}}/delete' class = 'class="btn text-secondary px-0'> Delete
    </a></button></td>

    <td><button><a href = '/{{object.pk}}/update' class = 'class="btn text-secondary px-0'> Update
  </a></button></td>
{% endblock content %}

template/sampleapp/employe_update_form.html

{% extends 'base.html' %}

{% block content %}
    <form method="post">
    {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Update">
    </form>
{% endblock content %}

template/sampleapp/employe_confirm_delete.html

{% extends 'base.html' %}

{% block content %}

    <form method="post">{% csrf_token %}

    <p>Are you sure you want to delete "{{ object }}"?</p>

    <input type="submit" value="Confirm">
</form>
{% endblock content %}

17.Conclusion:

In this tutorial, we have discussed about the class based views and how they are
different from function-based views. We have implemented the crud operations
using the built-in views.

The CBV is a powerful way to inherit from an existing view and override attributes
(template_name) or methods.

These views have prewritten code so we don't need to do the hard coding. But this
is not recommended for the beginners because it won't help to understand core
depth of the Django. Once you get familiar with the concept of function-based
views. You can shift towards class based views.
'''
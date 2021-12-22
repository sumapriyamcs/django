'''

1.Django Admin Interface:

Django provides a built-in admin module which can be used to perform CRUD
operations on the models. It reads metadata from the model to provide a quick
interface where the user can manage the content of the application.

This is a built-in module and designed to perform admin related tasks to the user.

Let's see how to activate and use Django's admin module (interface).

The admin app (django.contrib.admin) is enabled by default and already added
into INSTALLED_APPS section of the settings file.

To access it at browser use '/admin/' at a local machine like localhost:8000/admin/
It prompts for login credentials if no password is created yet, use the following command to create a user.

2.Create an Admin User:

$ python3 managen.py createsuperuser

Now start development server and access admin login.

$ python3 manage.py runserver

Provide created username and password and login.
It is a Django Admin Dashboard. Here, we can add and update the registered models.

'''
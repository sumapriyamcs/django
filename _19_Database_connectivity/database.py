'''
1.Django Database Connectivity:

The settings.py file contains all the project settings along with database
connection details. By default, Django works with SQLite, database and allows
configuring for other databases as well.

Database connectivity requires all the connection details such as database
name, user credentials, hostname drive name etc.

To connect with MySQL, django.db.backends.mysql driver is used to
establishing a connection between application and database. Let's see an example.

We need to provide all connection details in the settings file.
The settings.py file of our project contains the following code for the database.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoApp',
        'USER':'root',
        'PASSWORD':'mysql',
        'HOST':'localhost',
        'PORT':'3306'
    }
}

After providing details, check the connection using the migrate command.

$ python3 manage.py migrate

This command will create tables for admin, auth, contenttypes, and sessions

Now, access to the MySQL database and see the database from the list of databases.

#Note: It throws an error if database connectivity fails:
django.db.utils.OperationalError: (1045, "Access denied for user
'root'@'localhost' (using password: YES)")

2.Migrating Model:

Well, till here, we have learned to connect Django application to the
MySQL database. Next, we will see how to create a table using the model.

Each Django's model is mapped to a table in the database. So after creating
a model, we need to migrate it. Let's see an example.

Suppose, we have a model class Employee in the models.py file that contains the following code.

// models.py

from django.db import models
class Employee(models.Model):
    eid      = models.CharField(max_length=20)
    ename    = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"

Django first creates a migration file that contains the details of table structure.
To create migration use the following command.

$ python3 manage.py makemigrations

The created migration file is located into migrations folder and contains the following code.

from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
Now, migrate to reflect the changes into the database.

$ python3 manage.py migrate

Check the database again, now it contains the employee table.

See, a table is present in the database.
Well, we have successfully established a connection between our Django application and MySQL database.


'''
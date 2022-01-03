'''
1.The Database is the essential component of the web application to store and
organize the data. Whenever we develop an application/website, we need to choose
a suitable database that makes it more interactive.

Django comes with a built-in SQLite database. However, we can use the various
databases in Django. Below are the lists of databases that Django supports.

PostgreSQL
MariaDB
MySQL
Oracle
SQLite

There are also numbers of database backends provided by third parties.
Django middleware allows us to communicate with the database.
we will learn how we can connect the MySQL database to our Django application.

Prerequisites
MySQL server 5.7+ must be installed
Python 3.0+ must be installed

We assume that you have already installed the MySQL server on your local computer.
If you haven't installed then download it from MySQL official website.


2.Implementation:

We use the following steps to establish the connection between Django and MySQL.

Step - 1: Create a virtual environment and setting up the Django project

First we will create the virtual environment and install Django in it.
We skip this process as it lengthens the tutorial. We create the new project using the following command.

django-admin startproject MyProject .

The period (.) at the end of command indicates that we are creating the project
in the working directory. If the period is not provided, the project will be created
in the new directory named MyProject and inside that directory contains our actual django files.

Now start the server using the below command.

python manage.py runserver

The terminal will display the link http://127.0.0.1:8000, visit this link

Step - 2 Create new Database

We can create the Database using the two ways - MySQL Workbench and MySQL shell.
MySQL Workbench is a GUI tool for the MySQL database that provides features like
SQL development, data modeling and server administration. We will use the MySQL shell,
which is more recommended for learning purposes.


Connect MySQL Server
Create database using SQL queries
Use the create database my_database query. It will create the new database.
We can check the databases through the show databases query.

mysql> show databases;
+--------------------------------------+
| Database                                   |
+--------------------------------------+
| information_schema              |
| my_database                     |
| mysql                                          |
| performance_schema             |
| sys                                               |
+---------------------------------------+
5 rows in set (0.05 sec)
It shows the all available database in our MySQL server.


Step - 3: Update the settings.py

Once we are done creating the Database, we have to update the database section of
the settings.py file with the following setting configuration.


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
Let's understand what we have done above.

First, we have replaced the 'django.db.backends.sqlite3' to 'django.db.backends.mysql'.
This is basically indicating we shift SQLite to MySQL database.
NAME indicates the name of the database we want to use.
USER is the MYSQL username that has access to the Database and acts as a database administrator.
PASSWORD is the password of the database. It will be created at the time of MySQL installation.
'HOST' is '127.0.0.1' and 'PORT' '3306' points out that the MySQL databaseis hosted with the hostname
'0.0.1' and listens to the specific port number is 3306.

In the last line we use SET sql_mode = 'STATIC_TRANS_TABLES' which is used to handle the invalid
or missing values from being stored in the database by INSERT and UPDATE statements.

Step - 4 Install mysqlclient package

Before installing the mysqlclient package, let's understand what mysqlclient is and why we use.
The mysqlclient is the Python interface to MySQL that allows Python project to connect to the MySQL server.


So it is necessary to install mysqlclient package to establish the connection between the MySQL and Django.
To install, use the following command in the working directory.

pip install mysqlclient

Step - 5 Run the migrate command

Now we are ready to migrate or create tables in the newly created database. In this final step,
we will run the migrate command and it will create the exiting tables in the my_database database.

python manage.py migrate

After running this command Django will automatically create the necessary tables such as
auth_group, auth_user, auth_permission, etc. It will also create the tables which are
defined in the models.py file.

mysql> use my_database;

Database changed

mysql> show tables;

+-------------------------------------------------------+
| Tables_in_my_database                               |
+-------------------------------------------------------+
| auth_group                                                      |
| auth_group_permissions                               |
| auth_permission                                             |
| auth_user                                                         |
| auth_user_groups                                           |
| auth_user_user_permissions                        |
| django_admin_log                                           |
| django_content_type                                      |
| django_migrations                                           |
| django_session                                                |
| myweatherapp_profile                                   |
+---------------------------------------------------------+
11 rows in set (0.05 sec)


we have discussed how we can use the MySQL database in Django. Though Django comes with the
built-in database SQLite, sometimes it doesn't fulfill the requirements. So we can connect with
the various databases.



'''
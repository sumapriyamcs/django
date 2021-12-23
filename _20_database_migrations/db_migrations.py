'''
1.Django Database Migrations:

Migration is a way of applying changes that we have made to a model,
into the database schema. Django creates a migration file inside the migration
folder for each model to create the table schema, and each table is mapped to
the model of which migration is created.

Django provides the various commands that are used to perform migration related
tasks. After creating a model, we can use these commands.

1.makemigrations : It is used to create a migration file that contains code for
the tabled schema of a model.

2.migrate : It creates table according to the schema defined in the migration file.

3.sqlmigrate : It is used to show a raw SQL query of the applied migration.

4.showmigrations : It lists out all the migrations and their status.
Suppose, we have a model as given below and contains the following attributes.

2.Model:

//models.py

from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"

To create a migration for this model, use the following command. It will
create a migration file inside the migration folder.

$ python3 manage.py makemigrations

This migration file contains the code in which a Migration class
is created that contains the name and fields of employee table.

3.Migrations:

// 0001_initial.py

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
After creating a migration, migrate it so that it reflects the database permanently.
The migrate command is given below.

$ python3 manage.py migrate

Apart from creating a migration, we can see raw SQL query executing behind
the applied migration. The sqlmigrate app-name migration-name is used to get
raw SQL query. See an example.

$ python3 manage.py migrate

And showmigrations command is used to show applied migrations. See the example.

If no app-name is provided, it shows all migrations applied to the project.

$ python3 manage.py showmigrations

We can get app-specific migrations by specifying app-name, see the example.
$ python3 manage.py showmigrations myapp


'''
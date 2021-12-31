'''
1.Django ORM Queries | How to work with the ORM Queries:

Django ORM is one of the best tools of Django and plays very essential role to
perform database related tasks. It provides abstractions with the database,
in a mostly database agnostic way.

Django ORM consists of ease of use abstraction. It keeps "Simple things easy
and hard things possible."

2.Creating Table in Database using Model:

First, we will create a sample database using the Django model that consists of
some data and we will run the query on that database.

model.py

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

And then run the following command.

python manage.py makemigrations
python manage.py migrate

We are set to run the query.

'''
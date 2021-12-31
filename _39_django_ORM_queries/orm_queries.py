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

How to get all records from table(Model)
We have a model called Student. To get all records from model, we will use the
Student.objects.all(). To do so, open the Django shell to run the query.

>>> from sampleapp.models import Student
>>> queryset = Student.objects.all()
>>> queryset

<QuerySet [<Student: Ritesh Tiwari>, <Student: Yash Sharma>, <Student: Arpita Sharma>,
<Student: Prince Sharma>, <Student: Megha Bhardwaj>, <Student: Akash Mishra>]>

You might be wonder how Django ORM makes our queries executed or what the
corresponding query of the code we are writing. It is quite simple to get the
SQL query, we need to use the str() and pass the queryset object along with query.

Corresponding SQL Query

>>> str(queryset.query)

'SELECT "sampleapp_student"."id", "sampleapp_student"."username", "sampleapp_student".
"first_name", "sampleapp_student"."last_name", "sampleapp_student"."mobile",
"sampleapp_student"."email" FROM "sampleapp_student"'

You might be wonder how Django ORM makes our queries executed or what the
corresponding query of the code we are writing. It is quite simple to get the
SQL query, we need to use the str() and pass the queryset object along with query.

Corresponding SQL Query

>>> str(queryset.query)

'SELECT "sampleapp_student"."id", "sampleapp_student"."username",
"sampleapp_student"."first_name", "sampleapp_student"."last_name",
"sampleapp_student"."mobile", "sampleapp_student"."email" FROM "sampleapp_student"'

3.How to add record to table(Model):

We will use the Student.objects.create() and pass the fields along with its value as argument.

>>> queryset = Student.objects.create(username = 'rahul20', first_name = 'Rahul',
last_name = 'Shakya', mobile = '77777', email = 'rahul@gmail.com')
>>> queryset.save()

we need to use the .save() method on the query object to save the newly
created record in table, otherwise it will not show in database.

4.Retrieving Single Objects from QuerySets:

Suppose we need a specific object from a queryset to matching the result.
We can do this using the get() method. The get() returns the single object
directly. Let's see the following example.

Example -

>>> from sampleapp.models import Student
>>> queryset = Student.objects.get(pk = 1)
>>> queryset
<Student: Ritesh Tiwari>

Example - 2

>>> queryset = Student.objects.get(mobile = 22222)
>>> queryset
<Student: Yash Sharma>

As we can see in both examples, we get the single object not a queryset of a
single object. If there is no result then match the query, get() will raise
a DoesNotExist exception. On the other hand, if there is multiple field matches,
it will raise the MultipleObjectReturned, which is an attribute of the model class itself.

5.Filtering the Records:

In the earlier example, the QuerySet returned by all() describes the all record
in the database table. But sometimes, we need to select the subset of complete
set of object and it can be done by adding the filter conditions.

In the below example, we will fetch the data which first name starts with the R.

>>> queryset = Student.objects.filter(first_name__startswith = 'R')
>>> queryset
<QuerySet [<Student: Ritesh Tiwari>, <Student: Rahul Shakya>]>

>>> str(queryset.query)
'SELECT "sampleapp_student"."id", "sampleapp_student"."username",
"sampleapp_student"."first_name", "sampleapp_student"."last_name",
"sampleapp_student"."mobile", "sampleapp_student"."email" FROM "sampleapp_student"
WHERE "sampleapp_student"."first_name" LIKE R% ESCAPE \'\\\''

note:The difference between get() and filter() method is that, the filter()
method returns the queryset of object(s) where get() method returns single object.

6.Using exclude() Method:

It returns a new QuerySet containing objects that do not match the given
lookup parameter. In other words, it excluded the records according the lookup
condition. Let's understand the following example.

>>> queryset = Student.objects.exclude(first_name__startswith = 'R')
>>> queryset

Output:

, , , , ]>

7.How to make OR queries in Django ORM?

The OR operation is performed when we need the record filtering with two or
more conditions. In the below example, we will get the student whose first_name
starts with 'A' and last_name starts with 'M'.

Django allows us to do this in two ways.

queryset_1 |queryset_2
filter(Q(<condition_1>) | Q(<condition_2>

>>> queryset = Student.objects.filter(first_name__startswith = 'R') | Student.objects.filter
(last_name__startswith = 'S')
>>> queryset

<QuerySet [<Student: Ritesh Tiwari>, <Student: Yash Sharma>, <Student: Arpita Sharma>,
<Student: Prince Sharma>, <Student: Rahul Shakya>]>
We get the student details those first name starts with 'A' and last name starts with 'S'.

Let's the SQL query of corresponding OR operator.

>>> str(queryset.query)

'SELECT "sampleapp_student"."id", "sampleapp_student"."username", "sampleapp_student".
"first_name", "sampleapp_student"."last_name", "sampleapp_student"."mobile",
"sampleapp_student"."email" FROM "sampleapp_student" WHERE ("sampleapp_student".
"first_name" LIKE R% ESCAPE \'\\\' OR "sampleapp_student"."last_name" LIKE S% ESCAPE \'\\\')'

8.How to make AND queries in Django ORM?

The AND operation is performed when we need the record matching with two or more
conditions. In the below example, we will get the student whose first_name starts
with 'P' and last_name starts with 'S'.

Django allows us to do this in three ways.

queryset_1 & queryset_2
filter(<condition_1>, <condition_2>)
filter(Q(condition_1) & Q(condition_2))

>>> queryset = Student.objects.filter(first_name__startswith = 'P') & Student.objects.
filter(last_name__startswith = 'S')
>>> queryset
<QuerySet [<Student: Prince Sharma>]>
Only one object satisfied the given conditions.

We can also use the following query.

queryset2 = User.objects.filter( first_name__startswith='A', last_name__startswith='S' )

Or

queryset3 = User.objects.filter(Q(first_name__startswith='R') & Q(last_name__startswith='D') )
All queries will give the same result.

9.Creating Multiple Object in One Shot:

Sometimes we want create multiple objects in one shot. Suppose we want to create
new objects at once and we don't want to run the multiple queries to the database.
Django ORM provides the bulk_create to create multiple objects in one way.

>>> Student.objects.all().count()
7
Let's create the multiple records in one query.

Student.objects.bulk_create([Student(first_name = 'Jai', last_name = 'Shah',
mobile = '88888', email = 'shah@reddif.com'),Student(first_name = 'Tarak',
last_name = 'Mehta', mobile = '9999', email = 'tarak@reddif.com'),
Student(first_name = 'SuryaKumar', last_name = 'Yadav', mobile = '00000', email = 'yadav@reddif.com')])
[<Student: Jai Shah>, <Student: Tarak Mehta>, <Student: SuryaKumar Yadav>]

Now, our database table will update. The bulk_create takes a list of unsaved objects.
>>> Student.objects.all().count()
10

10.Limiting QuerySets:

We can set the limit on the queryset using the Python list's slicing syntax.
This is equivalent operation of SQL's LIMIT and OFFSET clauses. Let's see the following query.

>>> Student.objects.all()[:4]

<QuerySet [<Student: Ritesh Tiwari>, <Student: Yash Sharma>, <Student: Arpita Sharma>,
<Student: Prince Sharma>]>

Below query will return first record to fifth record.

>>> Student.objects.all()[1:6]
<QuerySet [<Student: Yash Sharma>, <Student: Arpita Sharma>, <Student: Prince Sharma>,
<Student: Megha Bhardwaj>, <Student: Akash Mishra>]>

Negative indexing is not supported. However, we can use the step in QuerySets.

>>> Student.objects.all()[:10:2]
[<Student: Ritesh Tiwari>, <Student: Arpita Sharma>, <Student: Megha Bhardwaj>,
<Student: Rahul Shakya>, <Student: Tarak Mehta>]

To fetching the single record, we can do the following operation.

>>> Student.objects.all()[0]
<Student: Ritesh Tiwari>

11.How to order a QuerySets in ascending or descending order?

Django provides the order_by method for ordering the queryset. This method takes
the field name which we want to Order (ascending and descending) the result.
Let's see the following example.

Example - Ascending order

>>> from sampleapp.models import Student
>>> Student.objects.all().order_by('mobile')

<QuerySet [<Student: SuryaKumar Yadav>, <Student: Ritesh Tiwari>,
<Student: Yash Sharma>, <Student: Arpita Sharma>, <Student: Prince Sharma>,
<Student: Megha Bhardwaj>, <Student: Akash Mishra>, <Student: Rahul Shakya>,
<Student: Jai Shah>, <Student: Tarak Mehta>]>

For descending order, we will use the Not '-' before the query field.

>>> from sampleapp.models import Student
>>> Student.objects.all().order_by('-mobile')
<QuerySet [<Student: Tarak Mehta>, <Student: Jai Shah>, <Student: Rahul Shakya>,
<Student: Akash Mishra>, <Student: Megha Bhardwaj>, <Student: Prince Sharma>,
<Student: Arpita Sharma>, <Student: Yash Sharma>, <Student: Ritesh Tiwari>,
<Student: SuryaKumar Yadav>]>

We can also pass the multiple fields in the order_by function.

>>> Student.objects.all().order_by('first_name','-mobile')
<QuerySet [<Student: Akash Mishra>, <Student: Arpita Sharma>, <Student: Jai Shah>,
<Student: Megha Bhardwaj>, <Student: Prince Sharma>, <Student:
Rahul Shakya>, <Student: Ritesh Tiwari>, <Student: SuryaKumar Yadav>, <Student: Tarak Mehta>,
<Student: Yash Sharma>]>

12.How to order on a field from a related model (with foreign key)?

Now, we will learn how we can order the data in the relation model. We create another
model called Teacher which is a related model of Student model.

Models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.teacher_name}'

class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    teacher_name = models.ForeignKey(Teacher, blank = True, null = True, on_delete= models.CASCADE)

We have added teachers name and each teacher is associated with the student.
Now we want to order Student by teacher_name inside each teacher_name by the
Student. We can do as follows.

>>> Student.objects.all().order_by('teacher__id', 'first_name')
<QuerySet [<Student: Prince Sharma>, <Student: Ritesh Tiwari>, <Student: SuryaKumar Yadav>,
<Student: Tarak Mehta>, <Student: Arpita Sharma>, <Student: Megha Bhardwaj>,
<Student: Jai Shah>, <Student: Rahul Shakya>, <Student: Yash Sharma>, <Student: Akash Mishra>]>

13.Important Field Lookups:

Query field lookups are nothing but a condition which specifies same as the
SQL WHERE clause. They are stated as keyword arguments to the QuerySet methods
such as filter(), exclude(), and get().

Example -

Student.objects.filter(first_name__startswith = 'Ritesh')
<QuerySet [<Student: Ritesh Tiwari>]>
This is same as the following SQL query

Select * from Student where first_name = "Ritesh"
Let's understand some important lookups.

exact
It returns the exact result according to the search.

>>> Student.objects.get(first_name__exact = 'Arpita')
<Student: Arpita Sharma>
Lookup should be used after the __ double underscore. We can use the
case-insensitive version called iexact.

contains
It is used to case-sensitive test. Let's see the following example.

>>> from sampleapp.models import Student
>>> Student.objects.filter(last_name__contains = 'Shar')

<QuerySet [<Student: Yash Sharma>, <Student: Arpita Sharma>, <Student: Prince Sharma>]>
If we translate the SQL query then it will look like as below.

SELECT ... WHERE last_name LIKE '%Shar%';
There is also case-incentive version called icontains.

How to perform join operations in Django
The SQL join combines data or rows from two or more tables based on a common
field between them. We can perform join operation in many ways.

>>> q = Student.objects.select_related('teacher')
>>>q
<QuerySet [<Student: Ritesh Tiwari>, <Student: Yash Sharma>, <Student: Arpita Sharma>,
<Student: Prince Sharma>, <Student: Megha Bhardwaj>, <Student: Akash Mishra>,
<Student: Rahul Shakya>, <Student: Jai Shah>, <Student: Tarak Mehta>, <Student: SuryaKumar Yadav>]>
>>>print(q.query)

SELECT "sampleapp_student"."id", "sampleapp_student"."username", "sampleapp_student".
"first_name", "sampleapp_student"."last_name", "sampleapp_student"."mobile",
"sampleapp_student"."email", "sampleapp_student"."teacher_id", "sampleapp_teacher".
"id", "sampleapp_teacher"."teacher_name" FROM "sampleapp_student"
LEFT OUTER JOIN "sampleapp_teacher" ON ("sampleapp_student"."teacher_id" = "sampleapp_teacher"."id")

15.How to group record in Django ORM?

Django ORM provides the grouping facility using the aggregation functions
like Max, Min, Avg, and Sum. Sometimes we need to get the aggregate values from the objects.

>>> from django.db.models import Avg, Max, Min, Sum, Count
>>> Student.objects.all().aggregate(Avg('id'))
{'id__avg': 5.5}
>>> Student.objects.all().aggregate(Min('id'))
{'id__min': 1}
>>> Student.objects.all().aggregate(Max('id'))
{'id__max': 10}
>>> Student.objects.all().aggregate(Sum('id'))
{'id__sum': 55}

16.How to perform truncate like operation using Django ORM?

Truncate in SQL means clear the table data for future use. Django doesn't
provide the built-in methods to truncate the table, but we can use the delete()
method to get the similar result.

>>> Student.objects.all().count()
10
>>> Student.objects.all().delete()
(10, {'sampleapp.Student': 10})
>>> Student.objects.all().count()
0
>>> Student.objects.all()
<QuerySet []>

If you want to delete the individual object instance, you need to call delete()
method on the individual instances of that model. We have called the delete()
method on model so it deleted the entire data.

17.How to get union of Data:

Union means getting the record which are common in both query sets

>>> q1 = Student.objects.filter(id__gte = 15)
>>> q1
<QuerySet [<Student: Megha Bhardwaj>, <Student: Akash Mishra>]>
>>> q2 = Student.objects.filter(id__lte = 15)
>>> q2

<QuerySet [<Student: Ritesh Tiwari>, <Student: Yash Sharma>,
<Student: Arpita Sharma>, <Student: Prince Sharma>, <Student: Megha Bhardwaj>]>

>>> q1.union(q2)
<QuerySet [<Student: Ritesh Tiwari>, <Student: Yash Sharma>,
<Student: Arpita Sharma>, <Student: Prince Sharma>, <Student: Megha Bhardwaj>,
<Student: Akash Mishra>]>

18.What is difference between null=True and blank=True?

we use null and blank often, by default their values are False.
Both of these value work at field level where we want to keep a field null or
blank. Both values seem similar but they are different in use.

If null=True means the field value is set as NULL i.e. no data.
It is basically for the database column value.

date = models.DateTimeField(null=True)

The blank = True specifies whether field is required in forms.

title = models.CharField(blank=True) // title can be kept blank.

In the database ("") will be stored.
If we set null=True blank=True, means that the field is optional in all circumstances.

teacher = models.ForeignKey(null=True, blank=True) // The exception is CharFields()
and TextFields(), which in Django are never saved as ?→NULL. Blank values are '
stored in the DB as an empty string ('').

Django ORM is a powerful tool and one of the key pillars of Django.
Django comes with the built-in database called SQLite. And we have described
the ORM queries which acts same as the SQL queries.

'''
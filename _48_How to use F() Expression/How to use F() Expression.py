'''
1.How to use F() Expression:

we will learn about the query expression, the F expression, and how to use it
in the QuerySet.

2.What is query expression?

Query expression signifies the value or a computational that can be a part of an update,
create, filter, order by, annotation or aggregate. If an expression returns the outputs
in Boolean, it may be used directly in filters. Django provides many built-in expressions
that help us to write queries. Query expression can be nested or combined.

3.Class F() Expression:

An F() object specifies the value of a model field, or it refers to the model field
values directly in the database. Let's have a simple example, A Student class with a
fees field, and we want to increase the 20 percent fees of the student.

It can be done as below.

student = Student.objects.all()
for stu in student:
    stu.fees *= 1.2

We can do this in the single query with the use of F() expression.

from django.db.models import F

Student.objects.update(fees=F('fees') * 1.2)
We can also use the following method.

student = Student.objects.get(pk=1)
student.price = F('fees') * 1.2
student.save()
But take care with this kind of assignment. The F() object persist after saving the model.

student.fees                   # fees = Decimal('10.00')
student.fees = F('fees') + 1
student.save()                  # fees = Decimal('11.00')
student.name = 'What the F()'
student.save()                  # fees = Decimal('12.00')

After the update of the field, that particular field will contain an instance of
django.db.models.expression.CombinedExpression, instead of actual result. We can access
the result immediately as follows.

student.fees= F('fees') + 1
product.save()
print(student.fees)            # <CombinedExpression: F(price) + Value(1)>
product.refresh_from_db()
print(student.fees)
We can also use the annotation of the data.

from django.db.models import ExpressionWrapper, DecimalField
Product.objects.all().annotate(
    value_in_stock=ExpressionWrapper(
        F('fees') * F('rollno'), output_field=DecimalField()
    )
)
Since fees is a DecimalField and rollno is an IntergerField, we need to wrap the
expression inside an ExpressionWrapper object.

It can be used to filter data as well.

Student.objects.filter(fees__gte=F(2000))

4.The F() expression can offer the following advantages.


It helps us to get the database, and restrict Python to access database.
It helps to reduce the number of queries for specific operation.

5.Avoiding race condition using F()

The F() expression also provides additional features like updating a field's
value avoids a race condition.

Let's understand it in a better way - If two Python threads execute the code,
the one thread could retrieve, increment, and save a field's value after the other
threads have retrieved it from the database. The value that is saved by the thread
will be based on the original value. The process of the first thread will be used.

Every time the database is involved in updating the field, the process will become more robust.
The F() expression will update the field based on the value of the field in the database
when the save() or update() is executed.

6.Using F() to sort null values:

We can sort the null values using the F() and nulls_first or nulls_last keyword
argument to asc() or desc() to control the ordering of a field's null values.

Let's see the below example to sort the students who haven't been paid fees after the new semester.


from django.db.models import F
Student.objects.order_by(F('fees_paid').desc(nulls_last=True))

7.Func() Expression:

Func() expression are involved in the database function such as COALESCE and
LOWER or aggregates like SUM. We can use them directly.

Example -

from django.db.models import F, Func
queryset.annotate(field_lower=Func(F('field'), function='LOWER'))

8.Aggregate Expressions:

The Aggregation expression is an important component of a Func() expression.
It informs the query that a GROUP BY clause is required. All aggregates function
inherits function inherits from Aggregate().

Example -

from django.db.models import Count
Student.objects.annotate(
    managers_required=(Count('num_employees') /8 ) + Count('num_managers'))

9.Value() Expression:

A Value() object represents the smallest component of an expression. We can represent
the integer, Boolean, or string values within the expression using the Value().

The Value() Expression is rarely used directly. When we write the expression
F('field') + 1, Django implicitly wraps the 1 in the Value(), allowing simple values
to be used in the more complex expression.

The value argument automatically includes the value in the expression, and these
values can be 1, True, or None. Django converts these Python values into their
corresponding database type. The output_field argument must be a model field instance
such as IntegerField() or BooleanField().

'''
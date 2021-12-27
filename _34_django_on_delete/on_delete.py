'''
1.Django on_delete:

Django offers many advantages and capabilities and changing the database
is one of its best benefits. Django framework can handle the backend process
effortlessly. Processes like creation, deletion, and update can be very flexible
performed by the Django models easily. In this tutorial, we have the complete
guide of the Django on_delete parameter.

The on_delete is one of the parameter which helps to perform database-related
task efficiently. This parameter is used when a relationship is established in
Django. The on_delete parameter allows us to work with the foreign key.

It is clear that whenever the foreign key concept comes into the scenario,
the on_delete parameter is expected to be declared as one among the parameters in the foreign key.

This parameter decides whether deletion must happen. It tells what to do when
a parent value is deleted. This option allows the extent of flexibility
to the database-oriented operations.

2.Syntax of Django on_delete:

field name = models.ForeignKey(WASD, on_delete = OPERATION TYPE)

The left-most value represents the field that is going to be created in reference.
We need to mention a specific field that will be used to perform the specific operation.
This field will pull the data from the parent field, and the parent field needs
to be mentioned here. It will reference the further through the framework.

In the database, the field_namewill act as the field inheriting the value of the foreign key.
On the right side, the ForeignKey()function represents the operation of foreign
key creation. To create the foreign in Django, this function is necessary to use.

Next, it takes several arguments that we will discuss in another tutorial,
and on_delete is one of them.The first argument, WASD, denotes the foreign key
which is expected to be inherited. Then, the on_deleteparameter is used,
which performs the various operations.

2.Various on-delete Options:

Django is famous for its robust relational management database management
system. The on_delete handle is used to handle the deletion of reference
data to maintain the database integrity.

The on_delete includes the following options -

CASCADE
PROTECT
SET_NULL
SET_DEFAULT
SET()
DO_NOTHING
CASCASE

When we set the on_delete parameter as CASCADE, deleting the reference object
will also delete the referred object. This option is most useful in many
relationships. Suppose a post has comments; when the Post is deleted, all
the comments on that Post will automatically delete. We don't want a comment
saving in the database when the associated Post is deleted.

3.PROTECT:

The PROTECT option behaves just opposite of CASCDE; if we try to delete the
actual reference object then all instance of the data on the reference object
are not deleted. In simple words, it prevents referenced object to be deleted
if it has an object referencing in database. If a post consists of comments,
it cannot be deleted.

If we forcefully delete the reference object, it will raise the ProtectedError
which can be handled in views.

2.SET_NULL:

First, we need to set the null option on the foreign key as True; we can use
the SET_NULL option on the on_delete option. When we delete the referenced object,
the referencing value will be updated as NULL. In simple words, a post is deleted
without deleting associated comments and set to be NULL.

3.SET_DEFAULT:

This option works the same as the name suggests; it takes the default value
set when defining the relationship. When we delete the referred object, then
the referencing object value will be assigned with the  default value that we
have created. When we delete the Post that has comments, the comments are
automatically assigned to the default post that we have created the model.

4.SET():

It is quite similar to the SET_DEFAULT, but provides more flexibility.
When we delete the referenced object then the referencing value is updated as NULL.
So a NULL value will be replaced for the referencing object.

5.DO_NOTHING:

As the name suggests, when we delete the referenced object, it does nothing.
It is not suggested to use because it violates the purpose of an RDBMS.
Comments are still referring to the deleted posts that do not even exist.
It causes a lot of bugs and data integrity errors.

6.RESTRICT:

The RESTRICT option is similar to the PROTECT option, but the only difference
is when we delete the reference object on_delete raise the RestrictedError.
But RESTRICT will provide the facility to delete the referenced object if the
referencing object and the object referred to objects are allotted with
reference to a different common object.

7.Example -Models.py file

from django.db import models

# Create your models here.

class Auther(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Post(models.Model):
    title = models.CharField(max_length=100)
    # Here we define the on_delete as CASCADE
    author = models.ForeignKey(Auther, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

We have created the two models, Author, and Post. In the post model, we define
a foreign key field named Author referencing the Author's object. Then we
define the on_delete parameter as CASCADE.

To display the models in the control panel, it needs to be registered in the admin.py file.

admin.py

from django.contrib import admin

from .models import Post, Author
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)

After creating the post and author, we have the following data in our database.
Now, we delete an author of book "You can win". After deleting this author,
associated post is also deleted automatically.

In the next example, we change the property of on_delete from CASCADE to
IS_NULL and migrate the database. Let's see how it is impact on database.

# Here we define the on_delete as IS_NULL
author = models.ForeignKey(Author, on_delete=models.SET_NULL, null = True)

We delete the author name "Mathew Barnard", the Post associated with
this Author will set as null

We have shown the two examples of on_delete options.
You can create your own models and apply each option and observe the result.

In this article, we have mentioned how we can use the on_delete parameter in
a foreign key. It provides the flexibility to delete the record and control
the impact of that deletion on the referenced records. It takes multiple options,
and each option allows us to control the behavior of referring data.

'''
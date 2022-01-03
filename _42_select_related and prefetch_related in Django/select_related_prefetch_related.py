'''
1.Django ORM stands for Object Relationship Mapper and it is used to
work with the database, and we can store the data in a Pythonic way

2.What is select_related in Django?

When we fetch any object from the database, it returns the new queryset consists
of that object not a particular object. It will create the new queryset of all
related objects on access time. This is not good in all cases.

Before moving the select_related operation, we should add below logging to the
setting.py file to see all SQL queries which are run behind in the Django CRM.

Merge the following snippet with the LOGGING field in your settings.py:

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}


Model.py

We create two models, a Movie and Director. The movie model has three fields,
including movie_title, release_year, and director foreign key.

from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete = models.CASCADE, max_length=100)

    def __str__(self):
        return self.name

Now we will run the following commands to make these tables in the database.

python manage.py makemigrations
python manage.py migrate

We will open the Django shell and create objects in order to store the date in tables.

python manage.py shell
Create the director objects in the Django shell.

from sampleapp.models import Director, Movie
director1 = Director.objects.create(name = "Steven Spiellberg")
director1.save()
director2 = Director.objects.create(name = "Christopher Nolan")
director2.save()
director3 = Director.objects.create(name = "Alan Taylor")
director3.save()
We get the queryset of directors using following commands.

 Director.objects.all()

(0.000) SELECT "sampleapp_director"."id", "sampleapp_director"."name" FROM
"sampleapp_director" LIMIT 21; args=()
<QuerySet [<Director: Steven Spiellberg>, <Director: Christopher Nolan>, <Director: Alan Taylor>]>

We can see the corresponding SQL query which is running internally.

Now we will create objects of the movie model.

movie1 = Movie.objects.create(name = "Super 8", release_year = '2011', director = director1)
(0.141) INSERT INTO "sampleapp_movie" ("movie_title", "release_year", "director_id")
VALUES ('Super 8', 2011, 1); args=['Super 8', 2011, 1]

movie1.save()

(0.172) UPDATE "sampleapp_movie" SET "movie_title" = 'Super 8', "release_year" = 2011,
"director_id" = 1 WHERE "sampleapp_movie"."id" = 1; args=('Super 8', 2011, 1, 1)

Above output displays the SQL queries of movie object. Same as we created the three movies objects.

from sampleapp.models import Director, Movie

Movie.objects.all()

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id" FROM "sampleapp_movie" LIMIT 21; args=()

<QuerySet [<Movie: Super 8>, <Movie: Ready Player One>, <Movie: Munich>, <Movie: The Terminal>,

The Movie table has the foreign key relationship with the Director table. So we
can use the following Query to fetch data

dir = Movie.objects.get(id = 2)

(0.016) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id" FROM "sampleapp_movie" WHERE "sampleapp_movie".
"id" = 2 LIMIT 21; args=(2,)

dir.director.name

(0.000) SELECT "sampleapp_director"."id", "sampleapp_director"."name" FROM "sampleapp_director"
WHERE "sampleapp_director"."id" = 2 LIMIT 21; args=(2,)

'Christopher Nolan'

As seen in the above code, we need to run a separate query to fetch the director
name using the Movie object.

These separate queries for the related objects decrease the performance of
an application. Suppose we have 1000 movies, and we have to create a list
of movies with the author's name.

Each time we access the foreign key, we need to make another query to retrieve
the value. So, we will end up running 1001queries to fetch the list of the books.

To overcome this problem, Django provides the select_related(), which will reduce the 1001 queries to 1.

9.Select Related:

The select_related performs the inner join operations in the table. In the below
example, movie_id is inner joined with the director.id.

Example -

movie = Movie.objects.select_related('director').all()

Let's create a query that fetches all movies with the name of the director in 1 query.

Open the Django shell and type the following query.

movies=Movie.objects.select_related('director').annotate(name=F('director__name')).
values('id', 'movie_title', 'name')
movies

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_director".
"name" AS "name" FROM "sampleapp_movie" INNER JOIN "sampleapp_director" ON
("sampleapp_movie"."director_id" = "sampleapp_director"."id") LIMIT 21; args=()
<QuerySet [{'id': 1, 'movie_title': 'Super 8', 'name': 'Steven Spiellberg'},
{'id': 2, 'movie_title': 'Ready Player One', 'name': 'Christopher Nolan'},
{'id': 3, 'movie_title': 'Munich', 'name': 'Alan Taylor'}, {'id': 4, 'movie_title':
'The Terminal', 'name': 'Steven Spiellberg'}, {'id': 5, 'movie_title': 'Game of Thrones',
'name': 'Alan Taylor'}, {'id': 6, 'movie_title': 'The Terminal', 'name': 'Alan Taylor'},
{'id': 7, 'movie_title': 'Super 8', 'name': 'Steven Spiellberg'}, {'id': 8, 'movie_title':
'Udan', 'name': 'Alan Taylor'}]>

As we can see in the output, only one join query has been called to fetch all movies with
the associate director. It is a big improvement for an application.

10.Difference Between select_related() and all()

Without select_related

Movie.objects.select_related('director').all()

(0.0)   SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id", "sampleapp_director"."id", "sampleapp_director".
"name" FROM "sampleapp_movie" INNER JOIN "sampleapp_director" ON ("sampleapp_movie".
"director_id" = "sampleapp_director"."id") LIMIT 21; args=()
(1.0)

<QuerySet [<Movie: Super 8>, <Movie: Ready Player One>, <Movie: Munich>, <Movie:
The Terminal>, <Movie: Game of Thrones>, <Movie: The Terminal>, <Movie: Super 8>, <Movie: Udan>]>

11.With select_related:

Now we will run the query with the all() method.

from sampleapp.models import Director, Movie
 Movie.objects.all()
(0.000)

SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie"."release_year",
"sampleapp_movie"."director_id" FROM "sampleapp_movie" LIMIT 21; args=()

<QuerySet [<Movie: Super 8>, <Movie: Ready Player One>, <Movie: Munich>, <Movie: The Terminal>,
<Movie: Game of Thrones>, <Movie: The Terminal>, <Movie: Super 8>, <Movie: Udan>]>
We get the same data from the both queries but there is a difference in the query lookups.

Let's have a look on another scenario where we want to get the director name of first movie.

11.Without select_related:

 Movie.objects.all()[0].director

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id" FROM "sampleapp_movie" LIMIT 1; args=()

(0.000) SELECT "sampleapp_director"."id", "sampleapp_director"."name" FROM "sampleapp_director"
WHERE "sampleapp_director"."id" = 1 LIMIT 21; args=(1,)
<Director: Steven Spiellberg>
We can observe that there are two SQL queries fired to fetch the director name. The
first query fetches the movie name, and the second query fetches the associated director name.
It may cause a lot of redundancy in the application. Let's see how we can do the same using a single query.

12.With select_related:

Movie.objects.select_related('director').all()[0].director

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id", "sampleapp_director"."id", "sampleapp_director".
"name" FROM "sampleapp_movie" INNER JOIN "sampleapp_director" ON ("sampleapp_movie"."director_id" =
"sampleapp_director"."id") LIMIT 1; args=()

<Director: Steven Spiellberg>
The select_related is only limited to foreign key relationship. If there is many to many
relationships then we cannot use the select_related. In that case, we can use the prefech_related.

13.Prefetch Related:

The prefetch_related can be used with the many to many relationships to improve
performance by reducing the number of queries. Let's understand the following example.

movies = Movie.objects.prefetch_related('publisher')
movies

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id" FROM "sampleapp_movie" LIMIT 21; args=()

(0.000) SELECT ("sampleapp_movie_publisher"."movie_id") AS "_prefetch_related_val_movie_id",
"sampleapp_director"."id", "sampleapp_director"."name" FROM "sampleapp_director" INNER JOIN
"sampleapp_movie_publisher" ON ("sampleapp_director"."id" = "sampleapp_movie_publisher"."director_id")
WHERE "sampleapp_movie_publisher"."movie_id" IN (1, 2, 3, 4, 5, 6, 7, 8); args=(1, 2, 3, 4, 5, 6, 7, 8)

<QuerySet [<Movie: Super 8>, <Movie: Ready Player One>, <Movie: Munich>, <Movie: The Terminal>,
<Movie: Game of Thrones>, <Movie: The Terminal>, <Movie: Super 8>, <Movie: Udan>]>

When we try to get the movie with the publisher, it runs the two SQL queries in the background

movie = Movie.objects.prefetch_related('publisher').all()[0].publisher

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie".
"release_year", "sampleapp_movie"."director_id" FROM "sampleapp_movie" LIMIT 1; args=()

(0.000) SELECT ("sampleapp_movie_publisher"."movie_id") AS "_prefetch_related_val_movie_id",
"sampleapp_director"."id", "sampleapp_director"."name" FROM "sampleapp_director" INNER JOIN
"sampleapp_movie_publisher" ON ("sampleapp_director"."id" = "sampleapp_movie_publisher"."director_id")
WHERE "sampleapp_movie_publisher"."movie_id" IN (1); args=(1,)

We can solve the problem using the prefetch_related(). Let's understand the following example.

movie = Movie.objects.prefetch_related('publisher').values('id', 'movie_title', 'publisher')
movie

(0.000) SELECT "sampleapp_movie"."id", "sampleapp_movie"."movie_title", "sampleapp_movie_publisher".
"director_id" FROM "sampleapp_movie" LEFT OUTER JOIN "sampleapp_movie_publisher" ON ("sampleapp_movie".
"id" = "sampleapp_movie_publisher"."movie_id") LIMIT 21; args=()

<QuerySet [{'id': 1, 'movie_title': 'Super 8', 'publisher': None}, {'id': 2, 'movie_title':
'Ready Player One', 'publisher': None}, {'id': 3, 'movie_title': 'Munich', 'publisher': None},
{'id': 4, 'movie_title': 'The Terminal', 'publisher': None}, {'id': 5,
'movie_title': 'Game of Thrones', 'publisher': None}, {'id': 6, 'movie_title':
'The Terminal', 'publisher': 1}, {'id': 6, 'movie_title': 'The Terminal', 'publisher': 2},
{'id': 6, 'movie_title': 'The Terminal', 'publisher': 3}, {'id': 7, 'movie_title': 'Super 8',
'publisher': 1}, {'id': 7, 'movie_title': 'Super 8', 'publisher': 2}, {'id': 8, 'movie_title':
'Udan', 'publisher': 1}, {'id': 8, 'movie_title': 'Udan', 'publisher': 2}]>


'movie_title': 'Game of Thrones', 'publisher': None}, {'id': 6, 'movie_title': 'The Terminal',
'publisher': 1}, {'id': 6, 'movie_title': 'The Terminal', 'publisher': 2}, {'id': 6, 'movie_title':
'The Terminal', 'publisher': 3}, {'id': 7, 'movie_title': 'Super 8', 'publisher': 1}, {'id': 7,
'movie_title': 'Super 8', 'publisher': 2}, {'id': 8, 'movie_title': 'Udan', 'publisher': 1},
{'id': 8, 'movie_title': 'Udan', 'publisher': 2}]>


'''
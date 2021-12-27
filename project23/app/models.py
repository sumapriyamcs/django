from django.db import models
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Post(models.Model):
    title = models.CharField(max_length=100)
    # Here we define the on_delete as CASCADE
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

#class delete(models.Model):
 #   title = models.CharField(max_length=100)
    # Here we define the on_delete as CASCADE
    #author = models.ForeignKey(Author, on_delete=models.CASCADE)
  #  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    #def __str__(self, retrun=None):
     #   retrun self.title

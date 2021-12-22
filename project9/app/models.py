from django.db import models

# Create your models here.
#from django.db import models
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=30)
    class Meta:
        db_table = "Student"


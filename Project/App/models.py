from django.db import models

# Create your models here.

# Create your models here.
#table ,columns
class Student(models.Model):  #table
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    section=models.IntegerField()
    roll_no=models.IntegerField()

    
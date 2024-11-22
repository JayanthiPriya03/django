#checks for the data type
#convert data to python data
#serialize the data

from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):  #table
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    section=serializers.IntegerField()
    roll_no=serializers.IntegerField()



    class Meta:
        model=Student
        fields="__all__" #to store the data into table
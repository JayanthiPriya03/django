from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from.serializers import StudentSerializers

# Create your views here.
#table- add data -post
class Sview(APIView):
    def post(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','students':serializer.data},status=200)
        else:
            return Response({"status":"error","data":serializer.data},status=status.HTTP_400_BAD_REQUEST)
        
        #get -to get data from the table
class Getview(APIView):
    def get(self,args,*kwargs):
        result=Student.objects.all()
        #result=Student.objects.get(id=id)
        serializer=StudentSerializers(result,many=True)
        return Response({'status':'success','students':serializer.data},status=200)




#delete
class Deleteview(APIView):
    def delete (self,request,id):
        student=Student.objects.get(id=id)
        student.delete() 
        serializer=StudentSerializers(student)
        return Response({'status':'success','students':serializer.data},status=200)

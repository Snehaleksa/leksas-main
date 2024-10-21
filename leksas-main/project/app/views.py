from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password
from .models import User,Student
from .serializers import PostSerializer,UserSerializer

# Create your views here.
def studentlog(data):
    user=User(username=data['username'],password=make_password(data['password']))
    user.save()
    return user
class StudentRegister(APIView):
  def post(self,request,format=None):
    try:
        student=request.data.get('student')
        print(student)
        data=request.data.get('data')
        print(data)
        stdlog=studentlog(student)
        print(stdlog)
        student_data=Student.objects.create(
            user_id=stdlog,
            name=data['name'],
            phone=data['phone'],
            address=data['address'],
            branch=data['branch'],
            rollno=data['rollno']
        )
        student_data.save()
        data1={"status":1}
        return JsonResponse(data1,safe=False)
        
    except Exception as e:
       print(e)
       data1={"status":0}
       return JsonResponse(data1,safe=False)
    

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "username": user.username,
        }
        try:
            personal_info = Student.objects.get(user_id=user)
            user_data["personal_info"] = {
                "Name": personal_info.name,
                "Phone": personal_info.phone,
                "Address": personal_info.address,
                "Branch": personal_info.branch,
                "Rollno": personal_info.rollno
            }
            return JsonResponse(user_data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            pass
        return JsonResponse({"message": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)


class UpdateProfile(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        try:
            personal_info = Student.objects.get(user_id=user)
        except Student.DoesNotExist:
            return JsonResponse({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = PostSerializer(personal_info, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
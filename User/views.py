from django.shortcuts import render
from django.http import JsonResponse
from requests import request
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method=="GET":
        user = User.objects.all()
        userserializer = UserSerializer(user, many=True)
        return JsonResponse(userserializer.data, safe=False)
    elif request.method=='POST':
        ##serializer = UserSerializer(data=request.data[])
        ##if serializer.is_valid():
        if User.objects.filter(username=request.data['username']).exists():
            user = User.objects.filter(username = request.data['username'])
            userserializer = UserSerializer(user, many=True)
            if userserializer.data[0]['blocked'] == True:
                return JsonResponse({"result":"blocked"})
            elif request.data['password'] == userserializer.data[0]['password']:
                return JsonResponse({'result':'logged in'})
            elif request.data['password'] != userserializer.data[0]['password']:
                return JsonResponse({"result": "invalid login details"})
        else:
            data = request.data
            User.objects.create(username=data['username'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'], email=data['email'])
            return JsonResponse({'result': 'user created'})
        ##else:
        ##    print(serializer.errors)
        ##    return JsonResponse({'result':'invalid input'})
    #user = User.objects.filter(username = request.data['username'])
    #userserializer = UserSerializer(user, many=True)
    #print(userserializer.data[0]['password'])
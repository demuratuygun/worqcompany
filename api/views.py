from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import User, Platform
from .serializers import UserSerializer, PlatformSerializer
from rest_framework import status


@api_view(['GET'])
def getUser(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getPlatform(request):
    users = Platform.objects.all()
    serializer = PlatformSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addPlatform(request):
    serializer = PlatformSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
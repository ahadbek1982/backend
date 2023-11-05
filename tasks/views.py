from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, permissions
from tasks.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Type_task, Otdels, Tasks
from .serializers import Type_taskSerializer, TasksSerializer, OtdelsSerializer
# @api_view(['GET', 'POST'])
from django.http import HttpResponse
# @permission_classes([IsAuthenticated])

def index(request):
    return HttpResponse("hello world")

class TasksViewset(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class OtdelsViewset(viewsets.ModelViewSet):
    queryset = Otdels.objects.all()
    serializer_class = OtdelsSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Type_taskViewset(viewsets.ModelViewSet):
    queryset = Type_task.objects.all()
    serializer_class = Type_taskSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

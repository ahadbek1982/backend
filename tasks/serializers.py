from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Type_task, Otdels, Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class OtdelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otdels
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class Type_taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_task
        fields = "__all__"

from django.shortcuts import render
from rest_framework import viewsets
from rp.models import Kategoriya
from rp.serializers import KategoriyaSerializer


class ListKatView(viewsets.ModelViewSet):
    serializer_class = KategoriyaSerializer
    queryset = Kategoriya.objects.all()

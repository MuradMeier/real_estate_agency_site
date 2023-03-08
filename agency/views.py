from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class LandPlotAPIView(generics.ListAPIView):
    queryset = LandPlot.objects.all()
    serializer_class = LandPlotSerializer


class FlatAPIView(ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class DetachedHouseAPIView(generics.ListAPIView):
    queryset = DetachedHouse.objects.all()
    serializer_class = FlatSerializer


class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

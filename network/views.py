# views.py

from rest_framework import viewsets
from .models import Track, Cable, Manhole, Segment, Duct, SubDuct
from .serializers import TrackSerializer, CableSerializer, ManholeSerializer, SegmentSerializer, DuctSerializer, \
    SubDuctSerializer
from django.shortcuts import render



class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class CableViewSet(viewsets.ModelViewSet):
    queryset = Cable.objects.all()
    serializer_class = CableSerializer


class ManholeViewSet(viewsets.ModelViewSet):
    queryset = Manhole.objects.all()
    serializer_class = ManholeSerializer


class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class DuctViewSet(viewsets.ModelViewSet):
    queryset = Duct.objects.all()
    serializer_class = DuctSerializer


class SubDuctViewSet(viewsets.ModelViewSet):
    queryset = SubDuct.objects.all()
    serializer_class = SubDuctSerializer


def map_view(request):
    return render(request, 'network/map.html')

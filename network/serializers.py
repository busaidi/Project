from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Track, Cable, Manhole, Segment, Duct, SubDuct


class TrackSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Track
        geo_field = "geometry"
        fields = ('id', 'name', 'geometry')


class CableSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Cable
        geo_field = "geometry"
        fields = ('id', 'name', 'geometry')


class ManholeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manhole
        fields = '__all__'


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = '__all__'


class DuctSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Duct
        geo_field = "geometry"
        fields = ('id', 'track', 'geometry')


class SubDuctSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SubDuct
        geo_field = "geometry"
        fields = ('id', 'duct', 'geometry')

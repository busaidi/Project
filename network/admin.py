# admin.py

from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import Track, Cable, Manhole, Segment, Duct, SubDuct

@admin.register(Track)
class TrackAdmin(gis_admin.GISModelAdmin):
    list_display = ('id', 'name', 'geometry')
    default_lon = 58.3992
    default_lat = 23.6143
    default_zoom = 12

@admin.register(Cable)
class CableAdmin(gis_admin.GISModelAdmin):
    list_display = ('id', 'name', 'geometry')
    default_lon = 58.3992
    default_lat = 23.6143
    default_zoom = 12

@admin.register(Manhole)
class ManholeAdmin(gis_admin.GISModelAdmin):
    list_display = ('id', 'name', 'location', 'track')
    default_lon = 58.3992
    default_lat = 23.6143
    default_zoom = 12

@admin.register(Segment)
class SegmentAdmin(gis_admin.GISModelAdmin):
    list_display = ('id', 'cable', 'start_manhole', 'end_manhole', 'geometry')
    default_lon = 58.3992
    default_lat = 23.6143
    default_zoom = 12

@admin.register(Duct)
class DuctAdmin(gis_admin.GISModelAdmin):
    list_display = ('id', 'track', 'geometry')
    default_lon = 58.3992
    default_lat = 23.6143
    default_zoom = 12

@admin.register(SubDuct)
class SubDuctAdmin(gis_admin.GISModelAdmin):
    list_display = ('id', 'duct', 'geometry')
    default_lon = 58.3992
    default_lat = 23.6143
    default_zoom = 12

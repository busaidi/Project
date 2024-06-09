# urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import TrackViewSet, CableViewSet, ManholeViewSet, SegmentViewSet, DuctViewSet, SubDuctViewSet


router = DefaultRouter()
router.register(r'tracks', TrackViewSet)
router.register(r'cables', CableViewSet)
router.register(r'manholes', ManholeViewSet)
router.register(r'segments', SegmentViewSet)
router.register(r'ducts', DuctViewSet)
router.register(r'subducts', SubDuctViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('map/', views.map_view, name='map'),
]


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from measurement.views import SensorViewSet, MeasurementViewSet

router1 = DefaultRouter()
router1.register('sensor', SensorViewSet)

router2 = DefaultRouter()
router2.register('temp', MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router1.urls + router2.urls

from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from measurement.views import SensorListView

router1 = DefaultRouter()
router1.register('sensor', SensorListView)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router1.urls


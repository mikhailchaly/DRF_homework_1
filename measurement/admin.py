from django.contrib import admin

# Register your models here.
from measurement.models import Measurement, Sensor

admin.site.register(Measurement)
admin.site.register(Sensor)
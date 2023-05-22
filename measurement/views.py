
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer



class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer




from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from . import models


class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes to be viewed 
    Why shouldn't Joe play poker in the savanna?
    Because, there are too many cheetahs there.

    """
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer
  
class ShoeColorSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes color to be viewed
    """
    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializer
  
class ShoeTypeSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes type to be viewed
    """
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializer


class ManufacturerTypeSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes type to be viewed
    """
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer

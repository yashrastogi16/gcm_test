from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# GCMDevice viewsets
class GCMDeviceViewSet(viewsets.ModelViewSet):
	queryset = GCMDevice.objects.all()
	serializer_class = GCMDeviceSerializer

@api_view(['GET', 'POST'])
def gcmdevice_list(request):
    """
    List all Gcmdevice, or create a new snippet.
    """
    if request.method == 'GET':
        gcmdevice = GCMDevice.objects.all()
        serializer = GCMDeviceSerializer(gcmdevice, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GCMDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
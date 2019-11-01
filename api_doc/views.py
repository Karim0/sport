from builtins import int

from django.shortcuts import render
from rest_framework.decorators import api_view, schema
from sport_app.models import SportSection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
import coreapi
from rest_framework.schemas import AutoSchema
from .serializers import Serializer


class SportSectionSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field('name', type='string', location='query', description='name'),
                coreapi.Field('info', type='string', location='query', description='info'),
                coreapi.Field('price', type='integer', location='query', description='price'),
                coreapi.Field('img', type='file', location="formData", description='img')
            ]

            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields


@api_view(['GET'])
def getAllSportSection(request):
    '''show All Sport Sections'''
    items = SportSection.objects.all()
    serializer = Serializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(SportSectionSchema())
def getSportSectionById(request):
    serializer = Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteSportSection(request, pk):
    item = SportSection.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(SportSectionSchema())
def updateSportSection(request, pk):
    item = SportSection.objects.get(id=pk)
    serializer = Serializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

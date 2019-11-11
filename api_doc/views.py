from django.shortcuts import render
from rest_framework.decorators import api_view, schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions, viewsets
from .serializers import *
from .schema import *


# ============== Rating ==============
@api_view(['GET'])
@schema(RatingSchema())
def getAllRatings(request):
    """show All Rating By SportSectionId"""
    items = Rating.objects.all()
    serializer = SerializerRating(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(RatingSchema())
def getRatingById(request, pk):
    """show All Rating By SportSectionId"""
    items = Rating.objects.filter(section_id=pk)
    serializer = SerializerRating(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(RatingSchema())
def addRating(request):
    serializer = SerializerRating(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(RatingSchema())
def deleteRating(request, pk):
    item = Rating.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(RatingSchema())
def updateRating(request, pk):
    item = Rating.objects.get(id=pk)
    serializer = SerializerRating(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ============== Comment ==============
@api_view(['GET'])
@schema(CommentSchema())
def getAllComment(request):
    """show All Comment By SportSectionId"""
    items = Comment.objects
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(CommentSchema())
def getCommentById(request, pk):
    """show All Comment By SportSectionId"""
    items = Comment.objects.filter(section_id=pk)
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(CommentSchema())
def addComment(request):
    serializer = SerializerComment(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(CommentSchema())
def deleteComment(request, pk):
    item = Comment.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(CommentSchema())
def updateComment(request, pk):
    item = Comment.objects.get(id=pk)
    serializer = SerializerComment(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@schema(CommentSchema())
def getCommentByCoachId(request, pk):
    """show All Comment By SportSectionId"""
    items = Comment.objects.filter(section_id=pk)
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(CommentSchema())
def addCommentToCoach(request):
    serializer = SerializerComment(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(CommentSchema())
def deleteCommentToCoach(request, pk):
    item = Comment.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(CommentSchema())
def updateCommentToCoach(request, pk):
    item = Comment.objects.get(id=pk)
    serializer = SerializerComment(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ============== Location ==============
@api_view(['GET'])
@schema(LocationSchema())
def getLocationBySectionId(request, pk):
    """show All Location By SectionId"""
    items = Location.objects.filter(section_id=pk)
    serializer = SerializerLocation(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(LocationSchema())
def addLocation(request):
    serializer = SerializerLocation(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(LocationSchema())
def deleteLocation(request, pk):
    item = Location.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(LocationSchema())
def updateLocation(request, pk):
    item = Location.objects.get(id=pk)
    serializer = SerializerLocation(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ============== Coach ==============
@api_view(['GET'])
def getCommentToCoachById(request, pk):
    """show All Review By CoachId"""
    items = ReviewToCoach.objects.filter(section_id=pk)
    serializer = SerializerReviewToCoach(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAllCoach(request):
    """show All Coach"""
    items = Coach.objects.all()
    serializer = SerializerCoach(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCoachesBySectionId(request, pk):
    """show All Coach"""
    items = Coach.objects.filter(location_id=pk)
    serializer = SerializerCoach(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCommentByCoachId(request, pk):
    """show All Coach"""
    items = Coach.objects.filter(id=pk)
    serializer = SerializerCoach(items, many=True)
    return Response(serializer.data)

#
# @api_view(['POST'])
# # @schema()
# def addCoach(request):
#     serializer = SerializerCoach(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteCoach(request, pk):
    item = Location.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
# @schema(SportSectionSchema())
def updateCoach(request, pk):
    item = Location.objects.get(id=pk)
    serializer = SerializerCoach(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ============== SportSection ==============
@api_view(['GET'])
@schema(SportSectionSchema())
def getSportSectionById(request, pk):
    items = SportSection.objects.filter(id=pk)
    serializer = SerializerSportSection(items, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSportSection(request, pk):
    item = SportSection.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(SportSectionSchema())
def updateSportSection(request, pk):
    item = SportSection.objects.get(id=pk)
    serializer = SerializerSportSection(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllSportSection(request):
    """show All Sport Sections"""
    items = SportSection.objects.all()
    serializer = SerializerSportSection(items, many=True)
    return Response(serializer.data)

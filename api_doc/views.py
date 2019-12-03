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
    """Возвращает все рейтинги"""
    items = Rating.objects.all()
    serializer = SerializerRating(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(RatingSchema())
def getRatingById(request, pk):
    """Возвращает список рейтингов по id секции"""
    items = Rating.objects.filter(section_id=pk)
    serializer = SerializerRating(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(RatingSchema())
def addRating(request):
    """Оценить секцию"""
    serializer = SerializerRating(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(RatingSchema())
def deleteRating(request, pk):
    """Отменить свою оценку"""
    item = Rating.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(RatingSchema())
def updateRating(request, pk):
    """Изменить свою оценку"""
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
    """Вернуть список коментов"""
    items = Comment.objects
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(CommentSchema())
def getAllCommentByType(request, typeComment):
    """Добавить комент по типу"""
    items = Comment.objects.filter(typeComment_id=typeComment)
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(CommentSchema())
def getAllCommentByTypeAndIdCon(request, typeComment, con_id):
    """Возвращает список комментов по типу и conn_id"""
    items = Comment.objects.filter(typeComment_id=typeComment, conn_id=con_id)
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(CommentSchema())
def getCommentById(request, pk):
    """Вызвращает коммент по id"""
    items = Comment.objects.filter(id=pk)
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(CommentSchema())
def addComment(request):
    """Добавть коммент"""
    serializer = SerializerComment(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(CommentSchema())
def deleteComment(request, pk):
    """Удалить коммент"""
    item = Comment.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(CommentSchema())
def updateComment(request, pk):
    """Изменить коммент"""
    item = Comment.objects.get(id=pk)
    serializer = SerializerComment(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@schema(CommentSchema())
def getCommentByCoachId(request, pk):
    """Список коментов по id коуча"""
    items = Comment.objects.filter(conn_id=pk, typeComment__name="Couch")
    serializer = SerializerComment(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(CommentSchema())
def addCommentToCoach(request):
    """Написать комент коучу"""
    serializer = SerializerComment(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(CommentSchema())
def deleteCommentToCoach(request, pk):
    """Удалить комент по id"""
    item = Comment.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(CommentSchema())
def updateCommentToCoach(request, pk):
    """Изменить комент по id"""
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
    """Изменить комент по id"""
    items = Location.objects.filter(section_id=pk)
    serializer = SerializerLocation(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(LocationSchema())
def addLocation(request):
    """Добавить локацию"""
    serializer = SerializerLocation(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@schema(LocationSchema())
def deleteLocation(request, pk):
    """Удалить локацию"""
    item = Location.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@schema(LocationSchema())
def updateLocation(request, pk):
    """Изменить локацию"""
    item = Location.objects.get(id=pk)
    serializer = SerializerLocation(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ============== Coach ==============

@api_view(['GET'])
def getAllCoach(request):
    """Список тренеров"""
    items = Coach.objects.all()
    serializer = SerializerCoach(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCoachesBySectionId(request, pk):
    """Возращает тренера по id"""
    items = Coach.objects.filter(location_id=pk)
    serializer = SerializerCoach(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCommentByCoachId(request, pk):
    """Возращает комент по id тренера"""
    items = Comment.objects.filter(conn_id=pk, typeComment__name="Coach")
    serializer = SerializerCoach(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(InfoAboutCoachSchema())
def addInfoAboutCoach(request):
    """Добавляет информацию о тренере"""
    if request.data:
        pk = request.data.get("id", 0)
        item = Coach.objects.filter(id=pk)
        if len(item) == 0:
            return Response("Такого тренера нет")
        item = item[0]
        item.info += " " + request.data.get('info', '')
        item.save()
        serializer = SerializerCoach(item, many=False)
        return Response(serializer.data)

    return Response("Что то пошло не так")


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
    """Возвращает спортивную секцию по id"""
    items = SportSection.objects.filter(id=pk)
    serializer = SerializerSportSection(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(SportSectionSchema())
def getSportSectionType(request):
    """Возвращает список типов спортивных секций"""
    items = SportSectionType.objects.all()
    serializer = SerializerSportSectionType(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@schema(SportSectionSchema())
def getSportSectionByTypeId(request, pk):
    """Возвращает список спортивных секций по id типа"""
    items = SportSection.objects.filter(type_id=pk)
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
    """Возвращает список спортивных секций"""
    items = SportSection.objects.all()
    serializer = SerializerSportSection(items, many=True)
    return Response(serializer.data)


# ============== TrainingSystems ==============
@api_view(['GET'])
def getAllTrainingSystems(request):
    """Возвращает список систем тренеровок"""
    items = TrainingSystem.objects.all()
    serializer = SerializerTrainingSystem(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTrainingSystemsById(request, pk):
    """Возвращает систему тренервки id"""
    items = TrainingSystem.objects.filter(id=pk)
    serializer = SerializerTrainingSystem(items, many=True)
    return Response(serializer.data)


# ============== Food ==============
@api_view(['GET'])
def getAllFood(request):
    """Возвращает список спортивного питания"""
    items = Food.objects.all()
    serializer = SerializerFood(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFoodById(request, pk):
    """Возвращает спортивное питание по id"""
    items = Food.objects.filter(id=pk)
    serializer = SerializerFood(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(CommentSchema())
def addCommentFood(request):
    """Добавляет коммент к спортивному питанию"""
    serializer = SerializerComment(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@schema(CommentSchema())
def updateCommentFood(request, pk):
    """Изменяет коммент к спортивному питанию по id комента"""
    item = Comment.objects.get(id=pk)
    serializer = SerializerComment(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteCommentFood(request, pk):
    """Удалить коммент к спортивному питанию по id комента"""
    item = Comment.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ============== Achievement ==============
@api_view(['GET'])
def getAllAchievement(request):
    items = Achievement.objects.all()
    serializer = SerializerAchievement(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAchievementById(request, pk):
    items = Achievement.objects.filter(id=pk)
    serializer = SerializerAchievement(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(FoodSchema())
def addAchievement(request):
    serializer = SerializerAchievement(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@schema(FoodSchema())
def updateAchievement(request, pk):
    item = Achievement.objects.get(id=pk)
    serializer = SerializerAchievement(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteAchievement(request, pk):
    item = Achievement.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ============== Reward ==============
@api_view(['GET'])
def getAllReward(request):
    items = Reward.objects.all()
    serializer = SerializerReward(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRewardById(request, pk):
    items = Reward.objects.filter(id=pk)
    serializer = SerializerReward(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@schema(RewardSchema())
def addReward(request):
    serializer = SerializerReward(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@schema(RewardSchema())
def updateReward(request, pk):
    item = Reward.objects.get(id=pk)
    serializer = SerializerReward(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteReward(request, pk):
    item = Reward.objects.get(id=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def buyGymMembership(request):
    pass


@api_view(['POST'])
def authUser(request):
    if request.method == "POST":
        users = User.objects.all()
        login = request.POST.get("login")
        password = request.POST.get("password")
        for i in users:
            if i.password == password and i.username == login:
                return Response("Success")

    return Response("Fail")


def addOrderFoodDelivery(request):
    pass

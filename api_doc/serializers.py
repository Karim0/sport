from rest_framework import serializers
from sport_app.models import *


class SerializerSportSection(serializers.ModelSerializer):
    class Meta:
        model = SportSection
        fields = '__all__'


class SerializerLocation(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class SerializerComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class SerializerRating(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class SerializerCoach(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class SerializerTypeComment(serializers.ModelSerializer):
    class Meta:
        model = TypeComment
        fields = '__all__'


class SerializerTrainingSystem(serializers.ModelSerializer):
    class Meta:
        model = TrainingSystem
        fields = '__all__'


class SerializerFood(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class SerializerAchievement(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class SerializerReward(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

#
# class SerializerReviewToCoach(serializers.ModelSerializer):
#     class Meta:
#         model = ReviewToCoach
#         fields = '__all__'

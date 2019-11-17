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

#
# class SerializerReviewToCoach(serializers.ModelSerializer):
#     class Meta:
#         model = ReviewToCoach
#         fields = '__all__'

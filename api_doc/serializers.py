from rest_framework import serializers
from sport_app.models import SportSection


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = SportSection
        fields = '__all__'

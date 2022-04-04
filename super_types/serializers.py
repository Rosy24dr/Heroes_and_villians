from rest_framework import serializers
from .models import SuperType


class super_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['super_type']
        
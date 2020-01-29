from rest_framework import serializers
from data.models import ClientData


class TimestampField(serializers.Field):
    """
    Converts database datetime value to milliseconds on serialization
    """
    def to_representation(self, value):
        return value.timestamp() * 1000

    def to_internal_value(self, value):
        return value


class ClientDataSerializer(serializers.Serializer):
    timestamp = TimestampField()
    value = serializers.IntegerField()

    def create(self, validatedData):
        return ClientData.objects.create(**validatedData)
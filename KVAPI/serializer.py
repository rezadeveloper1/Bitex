from rest_framework.serializers import ModelSerializer
from . import models


class KeyValueSerializer(ModelSerializer):
    class Meta:
        model = models.KeyValueModel
        fields = "__all__"
from rest_framework import serializers
from rp.models import Kategoriya


class KategoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = "__all__"

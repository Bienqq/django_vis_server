from rest_framework import serializers
from .models import PlotObject


class PlotObjectSerializer(serializers.HyperlinkedModelSerializer):
    share_url = serializers.ReadOnlyField()

    class Meta:
        model = PlotObject
        fields = ("id", "share_url", "formula", "start", "end", "step")





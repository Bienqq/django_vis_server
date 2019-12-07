from rest_framework import serializers
from .models import PlotObject, GraphObject


class PlotObjectSerializer(serializers.HyperlinkedModelSerializer):
    share_url = serializers.ReadOnlyField()

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'shareUrl': instance.share_url()
        }

    class Meta:
        model = PlotObject
        fields = ("id", "share_url", "formula", "start", "end", "step")


class GraphObjectSerializer(serializers.HyperlinkedModelSerializer):
    share_url = serializers.ReadOnlyField()

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'shareUrl': instance.share_url()
        }

    class Meta:
        model = GraphObject
        fields = ("id", "share_url", "connections", "nodes")

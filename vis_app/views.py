from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets

from .models import PlotObject, GraphObject
from .serializers import PlotObjectSerializer, GraphObjectSerializer


class PlotObjectView(viewsets.ModelViewSet):
    queryset = PlotObject.objects.all()
    serializer_class = PlotObjectSerializer


class GraphObjectView(viewsets.ModelViewSet):
    queryset = GraphObject.objects.all()
    serializer_class = GraphObjectSerializer


# For sharing visualisations
def vis_shared_plot(request, id):
    try:
        data = PlotObject.objects.get(pk=id)
        context = {
            'formula': data.formula,
            'start': data.start,
            'end': data.end,
            'step': data.step,
            'date_created': data.date_created
        }
        return render(request, 'vis-shared-plot.html', context)
    except ObjectDoesNotExist:
        return render(request, '404.html')


def vis_shared_graph(request, id):
    try:
        data = GraphObject.objects.get(pk=id)
        context = {
            'connections': data.connections,
            'nodes': data.nodes,
            "date_created": data.date_created
        }
        return render(request, 'vis-shared-graph.html', context)
    except ObjectDoesNotExist:
        return render(request, '404.html')

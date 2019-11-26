from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets

from .models import PlotObject
from .serializers import PlotObjectSerializer


class PlotObjectView(viewsets.ModelViewSet):
    queryset = PlotObject.objects.all()
    serializer_class = PlotObjectSerializer


# For sharing visualisations
def vis_shared(request, id):
    try:
        data = PlotObject.objects.get(pk=id)
    except ObjectDoesNotExist:
        return render(request, '404.html')

    context = {
        'formula': data.formula,
        'start': data.start,
        'end': data.end,
        'step': data.step,
        'date_created': data.date_created
    }
    return render(request, 'vis-shared.html', context)

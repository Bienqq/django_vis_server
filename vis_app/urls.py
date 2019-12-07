from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('vis-plot', views.PlotObjectView)
router.register('vis-graph', views.GraphObjectView)

urlpatterns = [
    path('', include(router.urls)),
    path('vis-shared-plot/<int:id>', views.vis_shared_plot, name='vis-shared'),
    path('vis-shared-graph/<int:id>', views.vis_shared_graph, name='vis-shared')
]
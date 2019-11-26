from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('vis', views.PlotObjectView)

urlpatterns = [
    path('', include(router.urls)),
    path('vis-shared/<int:id>', views.vis_shared, name='vis-shared')
]
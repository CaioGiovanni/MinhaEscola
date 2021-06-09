from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register(r'hora', views.HoraViewSet)
router.register(r'escola', views.EscolaViewSet)
router.register(r'avaliacao', views.AvaliacaoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

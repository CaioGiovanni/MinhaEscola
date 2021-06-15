from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register(r'hora', views.HoraViewSet)
router.register(r'escola', views.EscolaViewSet)
router.register(r'avaliacao', views.AvaliacaoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('escolaview/<int:pk>/', views.escolaView),
    path('novousuario/', views.novoUsuario),
    path('usuario/', views.perfilUsuario),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('usuariotoken/', views.usuarioToken)
]

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
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    ## Usuarios
    path('usuariotoken/', views.usuarioToken),
    path('usuario/', views.perfilUsuario),
    path('usuario/ler/', views.perfilUsuario),
    path('usuario/criar/', views.novoUsuario),
    path('usuario/atualizar/', views.atualizarUsuario),
    path('usuario/excluir/', views.excluirUsuario),
    path('usuario/recuperar/', views.recuperarUsuario),

    ## Avaliacao
    path('escola/criar/', views.criarEscola),
    path('escola/ler/', views.recuperarEscola),
    path('escola/atualizar/', views.atualizarEscola),
    path('escola/excluir/', views.excluirEscola),
    path('escola/importar/', views.importarEscolas),
    path('escola/calcular/', views.calcularNotaDasEscolas),

    ## Avaliacao
    path('avaliacoes/criar/', views.publicarAvaliacao),
    path('avaliacoes/ler/', views.recuperarAvaliacao),
    path('avaliacoes/atualizar/', views.atualizarAvaliacao),
    path('avaliacoes/excluir/', views.excluirAvaliacao),
]

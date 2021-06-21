from django.core.exceptions import ViewDoesNotExist
from django.db.models import query
from django.http.response import HttpResponse, JsonResponse
from django.template.response import *
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.views import exception_handler
from .models import Hora, Escola, Usuario, Avaliacao
from .serializers import EscolaSerializadorTemporario, HoraSerializador, EscolaSerializador, UsuarioSerializador, AvaliacaoSerializador, UserSerializador
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework_simplejwt.backends import TokenBackend
from .forms import *
# from .funcoesAuxiliares import vish

# Create your views here.

class HoraViewSet(viewsets.ReadOnlyModelViewSet):
  horaAtual = Hora()
  horaAtual.save()
  queryset = Hora.objects.all().order_by('-hora')
  serializer_class = HoraSerializador
  permission_classes = [permissions.AllowAny]

class EscolaViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Escola.objects.all()
  serializer_class = EscolaSerializador
  permission_classes = [permissions.AllowAny]

# class UsuarioViewSet(viewsets.ModelViewSet):
#   queryset = Usuario.objects.all()
#   serializer_class = UsuarioSerializador
#   permission_classes = [permissions.AllowAny]

class AvaliacaoViewSet(viewsets.ModelViewSet):
  queryset = Avaliacao.objects.all().order_by('rankingDaAvaliacao')
  serializer_class = AvaliacaoSerializador
  permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
  # sessaoAtual = self.request.user
  # queryset = User.objects.filter(username=sessaoAtual.get_username())
  queryset = User.objects.all()
  serializer_class = UserSerializador
  permission_classes = [permissions.IsAuthenticated]
  # def get_queryset(self):
  #   sessaoAtual = self.request.user
  #   queryset =  User.objects.filter(username=sessaoAtual.get_username())
    # return super().get_queryset()



## Funcao Inutil
@api_view(['GET'])
def escolaView(request, pk = 1):
  escola = Escola.objects.get(pk = pk)
  # escola = Escola.objects.filter(pk = pk)
  # escola = EscolaSerializadorTemporario(escola)
  serializador = EscolaSerializador(escola)

  return Response(serializador.data)
  # return JsonResponse(escola)
  # return Response({'vish':'vish', 'pk':pk})




### Funcoes do usuário
## TODO cadastrar o usuario
##/usuario/criar
@api_view(['GET','POST'])
def novoUsuario(request):
  try:
    if request.method == 'GET':
      formulario = UsuarioFormulario()
      return Response(formulario.clean_json())
    elif request.method == 'POST':
      formulario = UsuarioFormulario(request.data)
      if (formulario.is_valid()):
        if (formulario.is_avaliable()):
          return Response({'mensagem': 'O usuario agora está cadastrado.'})
        else:
          return Response({'mensagem': 'Email ou usuário já cadastrado.'})
      else:
        return Response({'mensagem': 'Não foi possível fazer o cadastro.'})
  except Exception as erro:
    print(erro)
    return Response({'mensagem': 'Vish 000: Houve um erro.'})

## TODO retornar o perfil
##/usuario/
##/usuario/ler
@api_view(['GET', 'POST'])
def perfilUsuario(request):
  try:
    if (request.user.is_authenticated):
      return Response ({'mensagem': 'Usuario autenticado.'})
    elif ('Authorization' in request.headers):
      try:
        return Response ({'mensagem': 'Usuario autenticado.'})
      except:
        return Response ({'mensagem': 'Vish 001: Usuário invalido.'})
    else:
      return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
  except Exception as erro:
    return Response({'mensagem': 'Vish 000: Houve um erro.'})
  # if (request.user.is_authenticated):
  #   user = request.user
  #   # usuario = user.body
  #   usuario = Usuario.objects.get(usuario = user)
  #   dicionarioEscola = {'nome': usuario.escolaAtual.nome, 'telefone': usuario.escolaAtual.telefone}
  #   dicionarioUsuario = {'nascimento': usuario.dataNascimento, 'cep': usuario.cep, 'telefone': usuario.telefone, 'escola':dicionarioEscola}
  #   return Response({'usuario':user.username, 'email':user.email, 'nome': user.first_name, 'sobrenome': user.last_name, 'usuario': dicionarioUsuario, 'erro':False})
  # else:
  #   return Response({'mensagem':'Você não está conectado', 'erro':True})


## TODO Atualizar o perfil
##/usuario/atualizar
@api_view(['GET','POST'])
def atualizarUsuario(request):
  try:
    if (request.method == 'POST'):
      if (request.user.is_authenticated):
        return Response ({'mensagem': 'Usuario autenticado.'})
      elif ('Authorization' in request.headers):
        try:
          return Response ({'mensagem': 'Usuario autenticado.'})
        except:
          return Response ({'mensagem': 'Vish 001: Usuário invalido.'})
      else:
        return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
    else:
      formulario = UsuarioFormulario()
      return Response(formulario.clean_json())
  except Exception as erro:
    return Response({'mensagem': 'Vish 000: Houve um erro.'})

## TODO marcar o perfil como inativo
##/usuario/excluir
@api_view(['GET','POST'])
def excluirUsuario(request):
  try:
    if (request.user.is_authenticated):
      return Response ({'mensagem': 'Perfil excluído.'})
    elif ('Authorization' in request.headers):
      try:
        return Response ({'mensagem': 'Perfil excluído.'})
      except:
        return Response ({'mensagem': 'Vish 001: Usuário invalido.'})
    else:
      return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
  except Exception as erro:
    return Response({'mensagem': 'Vish 000: Houve um erro.'})

## TODO recuperar usuário para o admin
##/usuario/recuperar
@api_view(['GET','POST'])
def recuperarUsuario(request):
  try:
    if (request.user.is_authenticated):
      if (request.user.is_superuser):
        return Response ({'mensagem': 'Usuario autenticado.'})
      else:
        return Response ({'mensagem': 'Usuario não tem permissão.'})
    elif ('Authorization' in request.headers):
      autenticacao = JWTAuthentication()
      usuario, token = autenticacao.authenticate(request)
      if (usuario.is_superuser):
        return Response ({'mensagem': 'Usuario autenticado.'})
      else:
        return Response ({'mensagem': 'Usuario não tem permissão.'})
    else:
      return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
  except Exception as erro:
    return Response({'mensagem': 'Vish 000: Houve um erro.'})


## Não serve para nada.
@api_view(['POST'])
def usuarioToken(request):
  headers = request.headers
  # print(headers)
  # token = headers['Authorization'].split(' ')[1]
  autenticacao = JWTAuthentication()
  # autenticacao = JWTTokenUserAuthentication()
  # token = str(token)
  # print(type(token))
  # print(token[0:10])
  # autenticacao.get_user(token)
  try:
    usuario, token = autenticacao.authenticate(request)
    # user = JWTTokenUserAuthentication.get_user(token)
    # vish()
    return Response({'mensagem': 'você está logado'})
  except:
    return Response({'mensagem': 'token invalido'})

##não serve para nada
@api_view(['GET', 'POST'])
def loginUsuario(request):
  try:
    pass
  except:
    pass


### Escola
# POST
# /escola/criar
# Create        = headers {Authorization} body {Escola} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def criarEscola(request):
  try:
    if (request.method == 'POST'):
      pass
    elif (request.method == 'GET'):
      formulario = EscolaFormulario()
      return Response(formulario.clean_json())
  except:
    pass

# GET
# /escola/ler/pkid
# Read          = {filtros} retorna {Escolas} ***
## TODO
@api_view(['GET'])
def recuperarEscola(request, idEscola, idAvaliacao):
  try:
    pass
  except:
    pass

# GET
# /escola/avaliacoes/pkid
# Read          = {filtros} retorna {Escolas} ***
## TODO
@api_view(['GET'])
def recuperarAvaliacoesDaEscola(request):
  try:
    pass
  except:
    pass


# POST
# /escola/atualizar
# Update        = headers {Authorization} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def atualizarEscola(request):
  try:
    pass
  except:
    pass

# POST
# /escola/excluir
# Delete        = headers {Authorization} body {filtros} retorna {mensagem} * ***
## TODO
@api_view(['GET','POST'])
def excluirEscola(request):
  try:
    pass
  except:
    pass

# POST
# /escola/importar
# Importar      = headers {Authorization} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def importarEscolas(request):
  try:
    pass
  except:
    pass

# POST
# /escola/calcular
# CalcularNotas = headers {Authorization} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def calcularNotaDasEscolas(request):
  try:
    pass
  except:
    pass

### Avaliações
# POST
# /avaliacoes/criar
# Create = headers {Authorization} body {Avaliação} retorna {mensagem} **
## TODO
@api_view(['GET','POST'])
def publicarAvaliacao(request):
  try:
    pass
  except:
    pass

# GET
# /avaliacoes/ler
# Read   = {Escola} retorna {Avaliações}
## TODO
@api_view(['GET'])
def recuperarAvaliacao(request, pk):
  try:
    pass
  except:
    pass

# POST
# /avaliacoes/atualizar
# Update = headers {Authorization} body {Avaliação} retorna {mensagem} **
## TODO
@api_view(['GET','POST'])
def atualizarAvaliacao(request):
  try:
    pass
  except:
    pass

# POST
# /avaliacoes/excluir
# Delete = headers {Authorization} body {Avaliação} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def excluirAvaliacao(request):
  try:
    pass
  except:
    pass
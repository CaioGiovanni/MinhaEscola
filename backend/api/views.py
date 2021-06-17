from django.core.exceptions import ViewDoesNotExist
from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework import permissions
from .models import Hora, Escola, Usuario, Avaliacao
from .serializers import EscolaSerializadorTemporario, HoraSerializador, EscolaSerializador, UsuarioSerializador, AvaliacaoSerializador, UserSerializador
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework_simplejwt.backends import TokenBackend
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

@api_view(['GET'])
def escolaView(request, pk = 1):
  escola = Escola.objects.get(pk = pk)
  escola = EscolaSerializadorTemporario(escola)
  return Response(escola)
  # return JsonResponse(escola)
  # return Response({'vish':'vish', 'pk':pk})

@api_view(['POST'])
def novoUsuario(request):
  pass

@api_view(['GET', 'POST'])
def loginUsuario(request):
  pass

@api_view(['GET'])
def perfilUsuario(request):
  if (request.user.is_authenticated):
    user = request.user
    # usuario = user.body
    usuario = Usuario.objects.get(usuario = user)
    dicionarioEscola = {'nome': usuario.escolaAtual.nome, 'telefone': usuario.escolaAtual.telefone}
    dicionarioUsuario = {'nascimento': usuario.dataNascimento, 'cep': usuario.cep, 'telefone': usuario.telefone, 'escola':dicionarioEscola}
    return Response({'usuario':user.username, 'email':user.email, 'nome': user.first_name, 'sobrenome': user.last_name, 'usuario': dicionarioUsuario, 'erro':False})
  else:
    return Response({'mensagem':'Você não está conectado', 'erro':True})

@api_view(['GET'])
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
  usuario, token = autenticacao.authenticate(request)
  # user = JWTTokenUserAuthentication.get_user(token)
  # vish()
  return Response({'mensagem': 'vish'})
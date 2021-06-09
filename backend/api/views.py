from django.core.exceptions import ViewDoesNotExist
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework import permissions
from .models import Hora, Escola, Usuario, Avaliacao
from .serializers import HoraSerializador, EscolaSerializador, UsuarioSerializador, AvaliacaoSerializador, UserSerializador
from django.utils import timezone
from django.contrib.auth.models import User

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

from .models import Escola, Usuario, Avaliacao, Hora
from rest_framework import serializers
from django.contrib.auth.models import User


class HoraSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Hora
    fields = ['hora']

class EscolaSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Escola
    fields = ['id', 'pk', 'nome', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'cep', 'telefone', 'descricao', 'site', 'foto', 'preAlfa', 'ensinoFundamental', 'ensinoMedio']

# class EscolaSerializadorUnitario(serializers.Serializer):
#   class Meta:
#     model = Escola
#     fields = ['nome', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'cep', 'telefone', 'descricao', 'site', 'foto', 'preAlfa', 'ensinoFundamental', 'ensinoMedio']

class UsuarioSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Usuario
    fields = ['usuario', 'dataNascimento', 'dataCadastro', 'escolaAtual', 'cep', 'telefone']

class AvaliacaoSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Avaliacao
    fields = ['ano', 'avaliador', 'escolaAvaliada', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'comentario', 'rankingDaAvaliacao']

class UserSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']

def EscolaSerializadorTemporario(instancia):
  return {'nome':instancia.nome}
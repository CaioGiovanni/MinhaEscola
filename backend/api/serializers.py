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
    fields = ['pk', 'nome', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'cep', 'telefone', 'descricao', 'site', 'foto', 'preAlfa', 'ensinoFundamental', 'ensinoMedio']

# class EscolaSerializadorUnitario(serializers.Serializer):
#   class Meta:
#     model = Escola
#     fields = ['nome', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'cep', 'telefone', 'descricao', 'site', 'foto', 'preAlfa', 'ensinoFundamental', 'ensinoMedio']



class UserSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'date_joined']

class UsuarioSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    usuario = UserSerializador
    model = Usuario
    fields = ['usuario', 'dataNascimento', 'dataCadastro', 'escolaAtual', 'cep', 'telefone']

class AvaliacaoSerializador(serializers.HyperlinkedModelSerializer):
  class Meta:
    escolaAvaliada = EscolaSerializador
    avaliador = UserSerializador
    model = Avaliacao
    # fields = ['pk', 'ano', 'avaliador', 'escolaAvaliada', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'comentario', 'rankingDaAvaliacao']
    fields = ['pk', 'ano', 'escolaAvaliada', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'comentario', 'rankingDaAvaliacao']
    # fields = ['pk', 'ano', 'estruturaEscolar', 'qualidadeEscolar', 'segurancaEscolar', 'alimentacaoEscolar', 'comentario', 'rankingDaAvaliacao']

def EscolaSerializadorTemporario(instancia):
  return {'nome':instancia.nome}

def SerializadorAlternativoUsuario(usuario):
  print(usuario)
  # userSerializado = UserSerializador(instancia)
  # userData = userSerializado.data
  usuarioCustom = Usuario.objects.get(pk = usuario['pk'])
  saida = {
    'usuario': usuario,
    'dataNascimento': usuarioCustom.dataNascimento,
    'dataCadastro': usuarioCustom.dataCadastro,
    'escolaAtual': usuarioCustom.escolaAtual,
    'cep': usuarioCustom.cep,
    'telefone': usuarioCustom.telefone
  }
  return saida
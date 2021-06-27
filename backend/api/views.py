from django.core.exceptions import ViewDoesNotExist
from django.db.models import query
from django.http.response import HttpResponse, JsonResponse
from django.template.response import *
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.views import exception_handler
from .models import Hora, Escola, Usuario, Avaliacao
from .serializers import EscolaSerializadorTemporario, HoraSerializador, EscolaSerializador, SerializadorAlternativoUsuario, UsuarioSerializador, AvaliacaoSerializador, UserSerializador
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
  permission_classes = [permissions.IsAdminUser]
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
## cadastrar o usuario
##/usuario/criar
@api_view(['GET','POST'])
def novoUsuario(request):
  try:
    if request.method == 'GET':
      formulario = UsuarioFormulario()
      return Response(formulario.clean_json())
    elif request.method == 'POST':
      formulario = UsuarioFormulario(request.data)
      # print(formulario)
      if (formulario.is_valid()):
        if (formulario.is_avaliable()):
          formulario.salvar_user()
          # usueeer = formulario.retornar_usuario()
          # print(usueeer)
          return Response({'mensagem': 'O usuario agora está cadastrado.'})
        else:
          return Response({'mensagem': 'Email ou usuário já cadastrado.'})
      else:
        return Response({'mensagem': 'Não foi possível fazer o cadastro.'})
  except Exception as erro:
    print(erro)
    return Response({'mensagem': 'Vish 000: Houve um erro.'})

## retornar o perfil
##/usuario/
##/usuario/ler
@api_view(['GET', 'POST'])
def perfilUsuario(request):
  try:
    if (request.user.is_authenticated):
      usuario = User.objects.get(username = request.user.username)
      userSerializado = UserSerializador(usuario).data
      usuarioCustom = Usuario.objects.get(pk = usuario.pk)
      # serializado = SerializadorAlternativoUsuario(userSerializado)
      serializado = UsuarioSerializador(usuarioCustom, context={'request': request})
      escola = EscolaSerializador(serializado['escolaAtual']).data
      serializado['escolaAtual'] = escola
      serializado['usuario'] = userSerializado
      return Response ({'mensagem': 'Usuario autenticado.', 'usuario':serializado})
    elif ('Authorization' in request.headers):
      try:
        autenticacao = JWTAuthentication()
        usuario, token = autenticacao.authenticate(request)
        userSerializado = UserSerializador(usuario).data
        usuarioCustom = Usuario.objects.get(pk = usuario.pk)
        # serializado = SerializadorAlternativoUsuario(userSerializado)
        serializado = UsuarioSerializador(usuarioCustom, context={'request': request}).data
        escola = EscolaSerializador(usuarioCustom.escolaAtual).data
        serializado['escolaAtual'] = escola
        serializado['usuario'] = userSerializado
        return Response ({'mensagem': 'Usuario autenticado.', 'usuario':serializado})
      except:
        return Response ({'mensagem': 'Vish 001: Usuário invalido.'})
    else:
      return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
  except Exception as erro:
    # print(erro)
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


## Atualizar o perfil
##/usuario/atualizar
@api_view(['GET','POST'])
def atualizarUsuario(request):
  try:
    if (request.method == 'POST'):
      formulario = UsuarioFormulario(request.data)
      usuario = User.objects.get(username = request.data['usuario'])
      # print(usuario.check_password(request.data['senha']))
      # print(request.data['novaSenha'] == request.data['confirmarSenha'])
      if (usuario.check_password(request.data['senha'])):
        if (request.data['novaSenha'] == request.data['confirmarSenha']):
          if (formulario.is_valid()):
            formulario.atualizar_user()
            return Response({'mensagem': 'Usuário atualizado.'})
          else:
            return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
        else:
          return Response({'mensagem': 'Vish 004: as senhas estão diferentes'})
      else:
        return Response({'mensagem': 'Vish 001: Usuário inválido'})

      # if (request.user.is_authenticated):

      #   if (True):
      #     formulario = UsuarioFormulario(request.data)
      #     return Response ({'mensagem': 'Usuario alterado.'})
      #   else:
      #     return Response ({'mensagem': 'Vish 003: Usuário não autenticado.'})
      # elif ('Authorization' in request.headers):
      #   try:
      #     autenticacao = JWTAuthentication()
      #     usuario, token = autenticacao.authenticate(request)
      #     return Response ({'mensagem': 'Usuario autenticado.'})
      #   except:
      #     return Response ({'mensagem': 'Vish 001: Usuário invalido.'})
      # else:
      #   return Response ({'mensagem': 'Vish 002: Formulario incorreto.'})
    else:
      formulario = UsuarioFormulario()
      return Response(formulario.clean_json())
  except Exception as erro:
    return Response({'mensagem': 'Vish 000: Houve um erro.'})

## TODO marcar o perfil como inativo
##/usuario/excluir
@api_view(['GET','POST'])
def excluirUsuario(request):
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
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
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
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
@api_view(['GET'])
def usuarioToken(request):
  headers = request.headers
  print()
  print(headers)
  print()
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
  return Response({'mensagem': 'Vish 667: Não estamos trabalhando nisso.'})
  try:
    pass
  except:
    pass


######### MENOR URGÊNCIA
### Escola
# POST
# /escola/criar
# Create        = headers {Authorization} body {Escola} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def criarEscola(request):
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
  try:
    if (request.method == 'POST'):
      if (request.user.is_authenticated and request.user.is_superuser):
        return Response({'mensagem': 'Escola criada'})
    elif (request.method == 'GET'):
      formulario = EscolaFormulario()
      return Response(formulario.clean_json())
  except:
    pass

## Prioridade
# GET
# /escola/ler/pkid
# Read          = {filtros} retorna {Escolas} ***
@api_view(['GET'])
def recuperarEscola(request, idEscola = 1):
  try:
    escola = Escola.objects.get(pk = idEscola)
    # print(escola)
    avaliacoes = Avaliacao.objects.filter(escolaAvaliada = escola) ## isso precisa estar em um try?
    escolaS = EscolaSerializador(escola)
    avaliacoesSerializadas = []
    for i in avaliacoes:
      data = AvaliacaoSerializador(i, context={'request': request}).data
      # print(i.avaliador)
      # data['usuario'] = UsuarioSerializador(i.avaliador, context={'request': request}).data
      data['avaliador'] = i.avaliador.pk
      data['usuario'] = "%s %s"%(i.avaliador.usuario.first_name, i.avaliador.usuario.last_name)
      avaliacoesSerializadas.append(data)
      # print(data)
    # print(avaliacoesSerializadas)
    return Response({'mensagem': 'Encontramos a escola.', 'escola': escolaS.data, 'avaliacoes': [avaliacoesSerializadas]})
  except Exception as erro:
    return Response({'mensagem': 'Vish 404: objeto não encontrado.'})

## Prioridade
# GET
# /escola/avaliacoes/pkid/pkid
# Read          = {filtros} retorna {Escolas} ***
@api_view(['GET'])
def recuperarAvaliacoesDaEscola(request, idEscola = 1, idAvaliacao = 1):
  try:
    escola = Escola.objects.get(pk = idEscola)
    escolaSerial = EscolaSerializador(escola, context={'request': request}).data
    avaliacao = Avaliacao.objects.get(pk = idAvaliacao)
    serializado = AvaliacaoSerializador(avaliacao, context={'request': request}).data
    serializado['escolaAvaliada'] = escolaSerial
    serializado['avaliador'] = avaliacao.avaliador.pk
    serializado['usuario'] = "%s %s"%(avaliacao.avaliador.usuario.first_name, avaliacao.avaliador.usuario.last_name)
    return Response({'mensagem': 'Encontramos a avaliação.', 'avaliacao': serializado})
  except:
    return Response({'mensagem': 'Vish 404: objeto não encontrado.'})


# POST
# /escola/atualizar
# Update        = headers {Authorization} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def atualizarEscola(request):
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
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
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
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
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
  try:
    pass
  except:
    pass

## Prioridade
# POST
# /escola/calcular
# CalcularNotas = headers {Authorization} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def calcularNotaDasEscolas(request):
  try:
    return Response({'mensagem': 'resolvido.'})
  except:
    return Response({'mensagem': 'Vish 000: Houve um erro.'})

def calcularNotaDaEscola(escola):
  avaliacoes = Avaliacao.objects.filter(escolaAvaliada = escola)
  estruturaEscolar = 0.0
  qualidadeEscolar = 0.0
  segurancaEscolar = 0.0
  alimentacaoEscolar = 0.0
  tamanho = float(len(avaliacoes))
  for i in avaliacoes:
    estruturaEscolar += (i.estruturaEscolar)/tamanho
    qualidadeEscolar += (i.qualidadeEscolar)/tamanho
    segurancaEscolar += (i.segurancaEscolar)/tamanho
    alimentacaoEscolar += (i.alimentacaoEscolar)/tamanho
  escola.estruturaEscolar = estruturaEscolar
  escola.qualidadeEscolar = qualidadeEscolar
  escola.segurancaEscolar = segurancaEscolar
  escola.alimentacaoEscolar = alimentacaoEscolar
  # escola.notaTotal = 5.0
  escola.save()

### Avaliações
# POST
# /avaliacoes/criar
# Create = headers {Authorization} body {Avaliação} retorna {mensagem} **
@api_view(['GET','POST'])
def publicarAvaliacao(request):
  try:
    if (request.method == 'POST'):
      formulario = AvaliacaoFormulario(request.data)
      # print(formulario.cleaned_data['avaliador'])
      # formulario.is_valid()
      # formulario.salvar()
      if (not formulario.is_valid()):
        return Response({'mensagem': 'Vish 003: formulário inválido'})
      elif (not formulario.is_avaliable()):
        return Response({'mensagem': 'Vish 007: esse formulario não é secreto'})
      elif (request.user.is_authenticated):
        usuario = request.user
        usuarioCustom = Usuario.objects.get(pk = usuario.pk)
        if (usuarioCustom == formulario.cleaned_data['avaliador'] and usuarioCustom.escolaAtual == formulario.cleaned_data['escolaAvaliada']):
          formulario.salvar()
          calcularNotaDaEscola(usuarioCustom.escolaAtual)
          return Response({'mensagem': 'resolvido.'})
        else:
          ({'mensagem': 'Vish 003: Usuário não autenticado.'})
      elif ('Authorization' in request.headers):
        autenticacao = JWTAuthentication()
        usuario, token = autenticacao.authenticate(request)
        usuarioCustom = Usuario.objects.get(pk = usuario.pk)
        if (usuarioCustom == formulario.cleaned_data['avaliador'] and usuarioCustom.escolaAtual == formulario.cleaned_data['escolaAvaliada']):
          formulario.salvar()
          calcularNotaDaEscola(usuarioCustom.escolaAtual)
          return Response({'mensagem': 'resolvido.'})
        else:
          return Response({'mensagem': 'Vish 003: Usuário não autenticado.'})
      else:
        return Response({'mensagem': 'Vish 001: Usuario não autenticado.'})
    else:
      return Response({'mensagem': 'Vish 101: erro no formulário'})
  except Exception as erro:
    print(erro)
    return Response({'mensagem': 'Vish 000: Houve um erro.'})


# GET
# /avaliacoes/ler/pkid
# Read   = {Escola} retorna {Avaliações}
@api_view(['GET'])
def recuperarAvaliacao(request, pk = 1):
  try:
    avaliacao = Avaliacao.objects.get(pk = pk)
    serializado = AvaliacaoSerializador(avaliacao, context={'request': request}).data
    escola = EscolaSerializador(avaliacao.escolaAvaliada, context={'request': request}).data
    
    serializado['escolaAvaliada'] = escola

    serializado['avaliador'] = avaliacao.avaliador.pk
    serializado['usuario'] = "%s %s"%(avaliacao.avaliador.usuario.first_name, avaliacao.avaliador.usuario.last_name)

    return Response({'mensagem': 'resolvido.', 'avaliacao':serializado})
  except Exception as erro:
    print(erro)
    return Response({'mensagem': 'Vish 000: Houve um erro.'})


# POST
# /avaliacoes/atualizar
# Update = headers {Authorization} body {Avaliação} retorna {mensagem} **
@api_view(['GET','POST'])
def atualizarAvaliacao(request):
  try:
    if (request.method == 'POST'):
      formulario = AvaliacaoFormulario(request.data)
      # print(formulario.cleaned_data['avaliador'])
      # formulario.is_valid()
      # formulario.salvar()
      if (not formulario.is_valid()):
        return Response({'mensagem': 'Vish 003: formulário inválido'})
      elif (formulario.is_avaliable()):
        return Response({'mensagem': 'Vish 404: objeto não encontrado'})
      elif (request.user.is_authenticated):
        usuario = request.user
        usuarioCustom = Usuario.objects.get(pk = usuario.pk)
        if (usuarioCustom == formulario.cleaned_data['avaliador'] and usuarioCustom.escolaAtual == formulario.cleaned_data['escolaAvaliada']):
          formulario.atualizar()
          calcularNotaDaEscola(usuarioCustom.escolaAtual)
          return Response({'mensagem': 'resolvido.'})
        else:
          ({'mensagem': 'Vish 003: Usuário não autenticado.'})
      elif ('Authorization' in request.headers):
        autenticacao = JWTAuthentication()
        usuario, token = autenticacao.authenticate(request)
        usuarioCustom = Usuario.objects.get(pk = usuario.pk)
        if (usuarioCustom == formulario.cleaned_data['avaliador'] and usuarioCustom.escolaAtual == formulario.cleaned_data['escolaAvaliada']):
          formulario.atualizar()
          calcularNotaDaEscola(usuarioCustom.escolaAtual)
          return Response({'mensagem': 'resolvido.'})
        else:
          return Response({'mensagem': 'Vish 003: Usuário não autenticado.'})
      else:
        return Response({'mensagem': 'Vish 001: Usuario não autenticado.'})
    else:
      return Response({'mensagem': 'Vish 101: erro no formulário'})
  except Exception as erro:
    print(erro)
    return Response({'mensagem': 'Vish 000: Houve um erro.'})


# POST
# /avaliacoes/excluir
# Delete = headers {Authorization} body {Avaliação} retorna {mensagem} *
## TODO
@api_view(['GET','POST'])
def excluirAvaliacao(request):
  return Response({'mensagem': 'Vish 666: Estamos trabalhando nisso.'})
  try:
    pass
  except:
    pass
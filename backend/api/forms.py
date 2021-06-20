from django import forms
from .models import *


### Usuario

## Serve para cadastro e atualizacao.
class UsuarioFormulario(forms.Form):
#   usuario = models.OneToOneField(User, related_name='usuário', on_delete=models.CASCADE)
  usuario = forms.CharField(label='usuario', max_length=20, required=True)
  nome = forms.CharField(label='nome', max_length=100, required=True)
  sobrenome = forms.CharField(label='sobrenome', max_length=100, required=True)
  senha = forms.CharField(label='senha', max_length=100, required=True)
  confirmarSenha = forms.CharField(label='senha', max_length=100, required=True)
  dataNascimento = forms.DateField(default=timezone.now(), required=True)
  # dataCadastro = forms.DateField(default=timezone.now())
  escolaAtual = forms.ForeignKey(Escola, on_delete=models.CASCADE, required=True)
  cep = forms.CharField(max_length=8, required=True)
  telefone = forms.CharField(max_length=11, required=True)

## Login, perfil, excluir
class UsuarioLogin(forms.Form):
  usuario = forms.CharField(label='usuario', max_length=20)
  senha = forms.CharField(label='senha', max_length=100)


## Recuperar informacao de usuarios. Precisa ser ADM
class UsuarioLogin(forms.Form):
  usuarioPesquisado = forms.CharField(label='usuario pesquisado', max_length=20)
  nomePesquisado = forms.CharField(label='usuario pesquisado', max_length=100)


### Escolas
## Criar e atualizar
class EscolaFormulario(forms.Form):
  nome = forms.CharField(label='nome', max_length=100, required=True)


### Avaliações
## Publicar e atualizar
class AvaliacaoFormulario(forms.Form):
  texto = forms.CharField(label='texto', max_length=100, required=True)

class AvaliacaoExcluir(forms.Form):
  escola = forms.CharField(label='nome da escola', max_length=100, required=True)
  usuarioPesquisado = forms.CharField(label='usuario pesquisado', max_length=20)
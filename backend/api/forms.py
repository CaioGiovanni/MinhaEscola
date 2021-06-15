from django import forms
from .models import *


class UsuarioFormulario(forms.Form):
#   usuario = models.OneToOneField(User, related_name='usuário', on_delete=models.CASCADE)
  usuario = forms.CharField(label='usuario', max_length=20)
  nome = forms.CharField(label='nome', max_length=100)
  sobrenome = forms.CharField(label='sobrenome', max_length=100)
  senha = forms.CharField(label='senha', max_length=100)
  dataNascimento = forms.DateField(default=timezone.now())
  dataCadastro = forms.DateField(default=timezone.now())
  escolaAtual = forms.ForeignKey(Escola, on_delete=models.CASCADE)
  cep = forms.CharField(max_length=8)
  telefone = forms.CharField(max_length=11)
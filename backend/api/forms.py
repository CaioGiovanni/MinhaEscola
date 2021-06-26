from django import forms
from .models import *
import random


### Usuario

## Serve para cadastro e atualizacao.
class UsuarioFormulario(forms.Form):
#   usuario = models.OneToOneField(User, related_name='usuário', on_delete=models.CASCADE)
  usuario = forms.CharField(label='usuario', max_length=20, required=True)
  nome = forms.CharField(label='nome', max_length=100, required=True)
  sobrenome = forms.CharField(label='sobrenome', max_length=100, required=True)
  email = forms.EmailField(label='email', max_length=100, required=True)
  senha = forms.CharField(label='senha', max_length=100, required=True)
  confirmarSenha = forms.CharField(label='senha', max_length=100, required=True)
  dataNascimento = forms.DateField()#required=True)
  # dataCadastro = forms.DateField(default=timezone.now())
  escolaAtual = forms.ModelChoiceField(queryset=Escola.objects.all())#, required=True)
  cep = forms.CharField(max_length=8, required=True)
  telefone = forms.CharField(max_length=11, required=True)

  def clean_json(self):
    return {"usuario":'',"nome":'',"sobrenome":'',"email":'',"senha":'',"confirmarSenha":'',"dataNascimento":'',"escolaAtual":'',"cep":'',"telefone":'',}
  
  def is_avaliable(self):
    nome_usuario = User.objects.filter(username = self.cleaned_data['usuario'])
    email_usuario = User.objects.filter(email = self.cleaned_data['email'])
    if (list(nome_usuario) == [] and list(email_usuario) == []):
      return True
    else:
      return False
  
  def salvar_user(self):
    # print(self.cleaned_data)
    usuario = self.cleaned_data['usuario']
    nome = self.cleaned_data['nome']
    sobrenome = self.cleaned_data['sobrenome']
    email = self.cleaned_data['email']
    senha = self.cleaned_data['senha']
    confirmarSenha = self.cleaned_data['confirmarSenha']
    
    
    # pk = User.objects.order_by('-pk')[0].pk + 1
    pk = random.randint(0, 1000000000)
    # print(pk)
    saida_user = User.objects.create_user(usuario, email, senha)
    saida_user.first_name = nome
    saida_user.last_name = sobrenome
    # saida_user = User(pk, username = usuario, first_name = nome, last_name = sobrenome, email = email, password = senha)
    saida_user.save()


    dataNascimento = self.cleaned_data['dataNascimento']
    escolaAtual = self.cleaned_data['escolaAtual']
    cep = self.cleaned_data['cep']
    telefone = self.cleaned_data['telefone']

    saida_usuario = Usuario(id = saida_user.id, usuario = saida_user, dataNascimento = dataNascimento, dataCadastro = saida_user.date_joined, escolaAtual = escolaAtual, cep = cep, telefone = telefone)
    saida_usuario.save()
  
  def atualizar_user(self):
    pass

## Login, perfil, excluir
class UsuarioLogin(forms.Form):
  usuario = forms.CharField(label='usuario', max_length=20)
  senha = forms.CharField(label='senha', max_length=100)

  def perfil_usuario(self):
    usuario = self.cleaned_data['usuario']
    senha = self.cleaned_data['senha']

    bancoUser = User.objects.get(username = usuario)
    bancoUsuario = Usuario.objects.get(pk = bancoUser.pk)
    return bancoUsuario


## Recuperar informacao de usuarios. Precisa ser ADM
class UsuarioPesquisar(forms.Form):
  usuarioPesquisado = forms.CharField(label='usuario pesquisado', max_length=20)
  nomePesquisado = forms.CharField(label='usuario pesquisado', max_length=100)
  
  def retornar_usuario(self):
    porUser = User.objects.filter(username = self.cleaned_data['usuarioPesquisado'])
    porNome = User.objects.filter(first_name = self.cleaned_data['nomePesquisado'])
    saida = porUser | porNome
    print(saida)
    return saida


### Escolas
## TODO
## Criar e atualizar
class EscolaFormulario(forms.Form):
  nome = forms.CharField(label='nome', max_length=256, required=True)
  cep = forms.CharField(max_length=8, required=True)
  telefone = forms.CharField(max_length=10)
  descricao = forms.CharField(max_length=4096)
  site = forms.CharField(max_length=2048)
  foto = forms.CharField(max_length=2048)
  preAlfa = forms.BooleanField()
  ensinoFundamental = forms.BooleanField()
  ensinoMedio = forms.BooleanField()

  def clean_json(self):
    return {}
  
  def is_avaliable(self):
    return True


### Avaliações
## TODO
## Publicar e atualizar
class AvaliacaoFormulario(forms.Form):
  texto = forms.CharField(label='texto', max_length=100, required=True)

  def clean_json(self):
    return {}

  def is_avaliable(self):
    return True

## Excluir publicacao
class AvaliacaoExcluir(forms.Form):
  escola = forms.CharField(label='nome da escola', max_length=100, required=True)
  usuarioPesquisado = forms.CharField(label='usuario pesquisado', max_length=20)
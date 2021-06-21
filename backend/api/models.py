from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Escola(models.Model):
  nome = models.CharField(max_length=256)
  estruturaEscolar = models.FloatField(default=0)
  qualidadeEscolar = models.FloatField(default=0)
  segurancaEscolar = models.FloatField(default=0)
  alimentacaoEscolar = models.FloatField(default=0)
  cep = models.CharField(max_length=8)
  telefone = models.CharField(max_length=10)
  descricao = models.CharField(max_length=4096, default = 'texto')
  site = models.CharField(max_length=2048, default = 'http')
  foto = models.CharField(max_length=2048, default = 'http')
  preAlfa = models.BooleanField(default=True)
  ensinoFundamental = models.BooleanField(default=True)
  ensinoMedio = models.BooleanField(default=True)

  def __str__(self):
    return self.nome

class Usuario(models.Model):
  usuario = models.OneToOneField(User, related_name='usuário', on_delete=models.CASCADE, blank=False)
  dataNascimento = models.DateField(default=timezone.now(), blank=False)
  dataCadastro = models.DateField(default=timezone.now())
  escolaAtual = models.ForeignKey(Escola, on_delete=models.CASCADE)
  cep = models.CharField(max_length=8)
  telefone = models.CharField(max_length=11)

  def __str__(self):
    return self.usuario

class Avaliacao(models.Model):
  ano = models.DateField(default=timezone.now())
  avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  escolaAvaliada = models.ForeignKey(Escola, on_delete=models.CASCADE)
  estruturaEscolar = models.IntegerField(default=0)
  qualidadeEscolar = models.IntegerField(default=0)
  segurancaEscolar = models.IntegerField(default=0)
  alimentacaoEscolar = models.IntegerField(default=0)
  comentario = models.CharField(max_length=256)
  rankingDaAvaliacao= models.FloatField(default=1)

  def __str__(self):
    return '%s, %s'%(self.avaliador.nome + self.escolaAvaliada.nome)

class Hora(models.Model):
  hora = models.DateTimeField(default=timezone.now())


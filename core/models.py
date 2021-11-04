from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Preletor(models.Model):
    id_preletor = models.AutoField(primary_key=True)
    nome_preletor = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.nome_preletor)

class Contato(models.Model):
    id_contato = models.AutoField (primary_key = True)
    nome_contato = models.CharField(max_length=255)
    num_contato = models.CharField(max_length=14)
    email_contato = models.EmailField(max_length=255)

    def __str__(self):
        return "%s" % (self.nome_contato)

class Eventos(models.Model):
    id_evento = models.AutoField (primary_key = True)
    nome_evento = models.CharField(max_length=55)
    dt_evento = models.DateField
    ingressantes = ManyToManyField(Contato, related_name="ingressantes")
    preletor = models.ForeignKey(Preletor, on_delete=models.CASCADE, related_name="preletor")
    
    def __str__(self):
        return "%s" % (self.nome_evento)
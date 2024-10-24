from django.db import models

class Insumo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    quantidade = models.IntegerField()
    unidade_medida = models.CharField(max_length=50) 
    limiar_minimo = models.IntegerField()
    limiar_maximo = models.IntegerField()

    def __str__(self):
        return self.nome

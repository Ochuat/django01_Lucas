from django.db import models

# Create your models here.
class Auau(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.DecimalField(max_digits=5, decimal_places=2)
    observacao = models.TextField()

    def __str__(self):
        return f'DogName: {self.nome} | Raça: {self.raca}'

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.DecimalField(max_digits=5, decimal_places=2)
    observacao = models.TextField()

    def __str__(self):
        return f'Tutor: {self.nome} | E-mail: {self.email}'


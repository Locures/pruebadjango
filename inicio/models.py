from django.db import models

# Create your models here.
class Auto(models.Model):
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=30)
    ano = models.IntegerField()
    nafta = models.IntegerField()
    
    def __str__(self):
        return f'{self.patente}{self.marca} - {self.nafta}'
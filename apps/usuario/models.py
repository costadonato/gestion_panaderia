from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    cuit = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.username}'

    def obtener_nombre_completo(self):
        if self.last_name and self.first_name:
            nombre_completo = f'{self.last_name}, {self.first_name}'
            return nombre_completo.strip()
        else:
            return self.username

    obtener_nombre_completo.short_description = 'Nombre Completo'

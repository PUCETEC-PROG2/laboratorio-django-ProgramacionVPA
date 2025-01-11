from django.db import models

# Create your models here.

class Pokemon(models.Model): 
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A','Agua'),
        ('F','Fuego'),
        ('T','Tierra'),
        ('P','Planta'),
        ('E','Eléctrico'),
        ('L','Lagartija'),
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField (max_digits=6, decimal_places=4)
    height = models.DecimalField (max_digits=6, decimal_places=4)
    
    def __str__(self):
        return self.name
    
## Entrenador
## Nombre
## Apellido
## Nivel
## Fecha de nacimiento DateField()

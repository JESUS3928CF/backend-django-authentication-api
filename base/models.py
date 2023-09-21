from django.db import models

# / Esto es para poder crear la dependencia del usuario con este modelo
from django.contrib.auth.models import User


# Create your models here.

# / Esto creara una nueva tabla en la db
class Note(models.Model):
    body = models.TextField(); #- aca estamos definiendo sus campos

    # - CASCADE, significa que si el usuario deja de existir sus notas también
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True) #- agrando una llave foránea con el usuario

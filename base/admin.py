from django.contrib import admin

# Register your models here.

# / Agregando el modelo al panel del admin
from .models import Note

admin.site.register(Note)
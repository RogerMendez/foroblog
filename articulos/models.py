from django.db import models
from contenidos.models import Contenido

class Articulo(models.Model):
	descripcion = models.TextField(verbose_name="Contenido del Articulo")
	contenido = models.ForeignKey(Contenido, null=True, blank=True)
	def __unicode__ (self):
		return self.contenido
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	area = models.CharField(max_length='50', verbose_name=u'Registre el Area')
	def __unicode__ (self):
		return self.area

class Contenido(models.Model):
	titulo = models.CharField(max_length='100', verbose_name=u'Registre el Titulo')
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	estado = models.BooleanField(default=False)
	reportado = models.BooleanField(default=False)
	usuario = models.ForeignKey(User, null=True)
	def __unicode__(self):
		return self.titulo
	class Meta:
		ordering = ["fecha_publicacion"]

class ContenidoCategoria(models.Model):
	categoria = models.ForeignKey(Categoria)
	contenido = models.ForeignKey(Contenido)
	def __unicode__(self):
		return self.contenido

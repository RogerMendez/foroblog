#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	avatar = models.ImageField(upload_to='avatares', verbose_name='Selecciones su Avatar', null=True)
	paices = (
		('BOLIVIA', 'BOLIVIA'),
		)
	pais = models.CharField(max_length='50', verbose_name='Seleccione su Pais', choices=paices, null=True)
	ciudades = (
		('SUCRE', 'SUCRE'),
		('LA PAZ', 'LA PAZ'),
		('POTOSI', 'POTOSI'),
		)
	ciudad = models.CharField(max_length='50', verbose_name=u'Seleccione su Ciudad', choices=ciudades, null=True)
	intereses = models.TextField(verbose_name=u'Descripcion de Interese', null=True)
	twitter = models.CharField(max_length="100", verbose_name=u'Twitter (sin @)')
	web = models.URLField(verbose_name=u'Sitio Web')
	firma = models.TextField(verbose_name=u'Firma', help_text='Este texto irá al final de tus mensajes')
	sexo = (
		('indefinido', 'Indefinido'),
		('masculino', 'Masculino'),
		('Femenino', 'Femenino'),
		)
	genero = models.CharField(max_length='50', choices=sexo)
	puntaje = models.IntegerField(default=0)
	usuario = models.ForeignKey(User, unique=True, null=True)
	completo = models.IntegerField(default=0)
	code_activation = models.CharField(max_length="100")
	def __unicode__(self):
		return self.usuario.username
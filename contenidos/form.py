from django.forms import ModelForm

from contenidos.models import Categoria, Contenido

class CategoriaForm(ModelForm):
	class Meta:
		model = Categoria

class ContenitoForm(ModelForm):
	class Meta: 
		model = Contenido
		exclude = ['estado', 'usuario', 'categoria', 'reportado']


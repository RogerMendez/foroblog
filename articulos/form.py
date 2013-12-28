from django.forms import ModelForm

from articulos.models import Articulo

class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo
		exclude=['contenido']
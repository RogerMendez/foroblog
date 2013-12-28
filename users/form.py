from django.forms import ModelForm
from django import forms
from users.models import Perfil
from django.contrib.auth.models import User

class EmailForm(forms.Form):
	email = forms.EmailField(label='Correo Electronico')


class PerfilForm(ModelForm):
	class Meta:
		model = Perfil
		exclude = ['completo', 'usuario', 'puntaje']

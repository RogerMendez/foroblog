from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from contenidos.models import Categoria, Contenido, ContenidoCategoria
from contenidos.form import CategoriaForm, ContenitoForm
from articulos.views import seleccion_categoria as articulos


def new_categoria(request, id_contenido, lugar):
	if request.method == 'POST':
		formulario = CategoriaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			#if lugar == 'libro':
			#	return HttpResponseRedirect(reverse(seleccion_categoria, args=(id_contenido)))
			#elif lugar == 'curso':
			#	return HttpResponseRedirect(reverse(selectcatecurso, args=(id_contenido)))
			#elif lugar == "articulo":
			#	return HttpResponseRedirect(reverse(selectarticulocat, args=(id_contenido,)))
			#else:
			return HttpResponseRedirect(reverse(articulos, args=(id_contenido)))
	else:
		formulario = CategoriaForm()
	return render_to_response('contenidos/new_categoria.html', {'formulario':formulario}, context_instance=RequestContext(request))

def add_categoria(request, id_contenido, id_categoria, lugar):
	ContenidoCategoria.objects.create(
		contenido_id = id_contenido,
		categoria_id = id_categoria,
		)
	#if lugar == 'libro':
	#	return HttpResponseRedirect(reverse(seleccion_categoria, args=(id_contenido,)))
	#elif lugar == 'curso':
	#	return HttpResponseRedirect(reverse(selectcatecurso, args=(id_contenido,)))
	#elif lugar == "articulo":
	#	return HttpResponseRedirect(reverse(selectarticulocat, args=(id_contenido,)))
	#else:
	return HttpResponseRedirect(reverse(articulos, args=(id_contenido,)))


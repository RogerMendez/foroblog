from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from contenidos.models import Categoria, Contenido, ContenidoCategoria

from contenidos.form import ContenitoForm
from articulos.form import ArticuloForm
from articulos.models import Articulo
from users.models import Perfil

@login_required(login_url="/login")
def seleccion_categoria(request, id_contenido):
	contenido = get_object_or_404(Contenido, pk = id_contenido)
	q1 = ContenidoCategoria.objects.filter(contenido=contenido)
	q2 = q1.values('categoria_id')	
	categoria = Categoria.objects.exclude(id__in = q2)#Categoria.objects.all()#select * from Categoria
	return render_to_response('articulo/select_categoria.html', {'categoria':categoria, 'contenido':contenido}, context_instance=RequestContext(request))

@login_required(login_url="/login")
def new_articulo(request):
	if request.method == 'POST':
		formulariocontenido = ContenitoForm(request.POST)
		formularioarticulo = ArticuloForm(request.POST)
		if formulariocontenido.is_valid() and formularioarticulo.is_valid():
			contenido = formulariocontenido.save()
			contenido.usuario = request.user
			contenido.save()
			arti = formularioarticulo.save()
			arti.contenido = contenido
			arti.save()
			return HttpResponseRedirect(reverse(seleccion_categoria, args=(contenido.id,)))
	else:
		formulariocontenido = ContenitoForm()
		formularioarticulo = ArticuloForm()
	return render_to_response('articulo/new_articulo.html', {'formularioarticulo':formularioarticulo, 'formulariocontenido':formulariocontenido}, context_instance=RequestContext(request))

@login_required(login_url="/login")
def misarticulos(request):
	conte = Contenido.objects.filter(usuario = request.user)
	q2 = conte.values('id')
	misarticulos = Articulo.objects.filter(contenido_id__in = q2)
	q1 = misarticulos.values('contenido_id')
	contenidos = Contenido.objects.filter(id__in = q1)
	return render_to_response('articulo/listado_articulo.html', {'misarticulos':misarticulos, 'contenidos':contenidos}, context_instance=RequestContext(request))
@login_required(login_url="/login")
def articulo_detalle(request, id_articulo):
	art = get_object_or_404(Articulo, pk = id_articulo)
	contenido = Contenido.objects.get(pk = art.contenido_id)
	usuario = User.objects.get(pk = contenido.usuario_id)
	categorias = ContenidoCategoria.objects.filter(contenido = contenido)
	perfil = Perfil.objects.get(usuario_id = usuario.id)
	return render_to_response('articulo/detalle_articulo.html', {
										'articulo':art,
									 	'contenido':contenido, 
								 		'usuario':usuario,
								 		'perfil':perfil,
								 		'descri':descri,
								 		'categorias':categorias,
											},
										  context_instance=RequestContext(request))


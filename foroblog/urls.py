from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'users.views.index'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),

	#USUARIOS
	url(r'^user/new/$', 'users.views.new_user'),
	url(r'^user/confirmar/$', 'users.views.confirmation_user'),
	url(r'^login/$', 'users.views.loguet_in'),
	url(r'^logout/$', 'users.views.loguet_out'),
	url(r'^perfil/$', 'users.views.private'),

	#CONTENIDOS
	url(r'^categoria/new/(?P<id_contenido>\d+)/(?P<lugar>.*)/$', 'contenidos.views.new_categoria'),
	url(r'^categoria/add/(?P<id_contenido>\d+)/(?P<id_categoria>\d+)/(?P<lugar>.*)/$', 'contenidos.views.add_categoria'),

	#ARTICULOS
	url(r'^articulo/categoria/(?P<id_contenido>\d+)/$', 'articulos.views.seleccion_categoria'),
    url(r'^articulo/new/$', 'articulos.views.new_articulo'),
    url(r'^articulo/listado/$', 'articulos.views.misarticulos'),
)

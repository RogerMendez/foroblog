#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from users.models import Perfil
from users.form import EmailForm

import random

def code_activation_create():
    li = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0']
    #51 elementos
    code = random.choice(li)
    for i in range(50):
        code += random.choice(li)
    return code

def index(request):
    return render_to_response('base.html', context_instance=RequestContext(request))


def new_user(request):
    if request.method == 'POST':
        formuser = UserCreationForm(request.POST)
        formemail = EmailForm(request.POST)
        if formemail.is_valid() and formuser.is_valid() :
            code = code_activation_create()
            email = formemail.cleaned_data['email']
            u = formuser.save()
            u.email = email
            u.is_active = False
            u.save()
            Perfil.objects.create(
                usuario = u,
                code_activation = code,
            )
            subject = 'Confirmacion De Cuenta'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = '<h2>Confirmacion de Correo</h2><p>Haga click en el siguiente Enlace</p><p><a href="http://127.0.0.1:8000/user/confirmar/?code='+code+'">Confirmar Cuenta</a></p>'
            from_email = '"RoRaRo" <sieboliva@gmail.com>'
            to = email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            msm = "Su cuenta fue creada Correctamente<br><h2>Un Mensaje fue enviado a su correo para activar su cuenta</h2>" 
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect('/')
    else:
        formuser = UserCreationForm()
        formemail = EmailForm()
    return render_to_response('users/new_user.html',{
        'formuser':formuser,
        'formemail':formemail,
        },context_instance=RequestContext(request))

def confirmation_user(request):
    code = request.GET['code']
    if Perfil.objects.filter(code_activation = code):
        perfil = Perfil.objects.get(code_activation = code)
        usuario = User.objects.get(perfil__code_activation = code)
        usuario.is_active = True
        usuario.save()
        perfil.code_activation += usuario.username
        perfil.save()
        msm = 'Su cuenta fue Activada Correctamente<br><p><a href="http://127.0.0.1:8000/">Iniciar Sesion</a></p>' 
        messages.add_message(request, messages.INFO, msm)  
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(reverse(new_user))



def loguet_in(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(private))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        return HttpResponseRedirect(reverse(private))
                else:
                    msm = 'Su Cuenta no Esta Activada<br><p class="lead">Active su Cuenta Desde El Mensaje Enviado a Su Correo</p>'
                    messages.add_message(request, messages.INFO, msm) 
                    return HttpResponseRedirect(reverse(loguet_in))
            else:
                msm = 'Usted No es Usuario del Sistema<br><p><a href="http://127.0.0.1:8000/user/new/">Registrese</a></p>'
                messages.add_message(request, messages.INFO, msm) 
                return HttpResponseRedirect(reverse(loguet_in))
    else:
        formulario = AuthenticationForm()
    return render_to_response('users/login.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url="/login")
def loguet_out(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url="/login")
def private(request) :
    usuario = request.user
    perfil = Perfil.objects.get(usuario = usuario)
    return render_to_response('users/perfil.html', {
        'usuario' :usuario,
        'perfil':perfil,
        }, context_instance=RequestContext(request))

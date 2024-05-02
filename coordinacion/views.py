from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Detallesolicitud
from django.urls import reverse


# Create your views here.
def inicio_coordinacion(request):
    return render(request, 'vistas/inicio_coordinacion.html',{
        'tituloventana': "Inicio"
    })
def noticias(request):
    #noticias = Detallesolicitud.objects.all()  # Obtener todas las noticias
    # cordi_noti = reverse('vistas/noticias.html')
    # return redirect(cordi_noti)
    return render(request,'vistas/noticias.html')




def editar_noticia(request, id):
    noticia = get_object_or_404(Detallesolicitud, pk=id)

    return render(request, 'editar_noticia.html', {'form': form})






def actualizarperfil(request) :
    return render(request, 'vistas/actualizarperfil.html')





def registro_coordinacion(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from .models import Publicacion

def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs':pubs})

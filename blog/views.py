from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
# Create your views here.
from .models import Publicacion

from .forms import FormPub

def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs':pubs})

def detalle_pub(request, pk):
    p = get_object_or_404(Publicacion, pk = pk)
    return render(request, 'blog/detalle_pub.html', {'p':p})

def nueva_pub(request):
    if request.method == "POST":
        f = FormPub(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            # p.texto = request.texto
            p.fecha_publicacion = timezone.now()
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = FormPub()
    return render(request, 'blog/nueva_pub.html', {'formulario': f})

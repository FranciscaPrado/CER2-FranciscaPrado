from django.shortcuts import render
from core.models import correspondencia
from django.shortcuts import render
 
def LibroView(request):
    libro = Correspondencia.objects.filter(numero_res = True)
    return render(request, 'base.html', {'obj':libro})

def base(request):
    Correspondencia = correspondencia.objects.all()
    data = {'Correspondencia': Correspondencia}
    return render(request, "core/base.html", data)
# Create your views here.

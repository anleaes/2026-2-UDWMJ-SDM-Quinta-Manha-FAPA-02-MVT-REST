from django.shortcuts import render, redirect, get_object_or_404
from .forms import CupomForm
from .models import Cupom
from rest_framework import viewsets
from .serializer import CupomSerializer

def criar_cupom(request):
    template_name = 'cupom/criar_cupom.html'
    context={}

    if request.method == 'POST':
        form = CupomForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('cupom:lista_cupom')
    form = CupomForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_cupom(request):
    template_name = 'cupom/lista_cupom.html'
    cupom= Cupom.objects.prefetch_related('eventos_validos')
    context = {
        'cupom': cupom
    }
    return render(request, template_name, context)

def editar_cupom(request, id_cupom):
    template_name = 'cupom/criar_cupom.html'
    context={}
    cupom = get_object_or_404(Cupom, id=id_cupom)
    if request.method == 'POST':
        form = CupomForm(request.POST, instance=cupom)
        if form.is_valid():
            form.save()
            return redirect('cupom:lista_cupom')
    form = CupomForm(instance=cupom)
    context['form'] = form
    return render(request, template_name, context)

def deletar_cupom(request, id_cupom):
    cupom = Cupom.objects.get(id=id_cupom)
    cupom.delete()
    return redirect('cupom:lista_cupom')

class CupomViewSet(viewsets.ModelViewSet):
    queryset = Cupom.objects.all()
    serializer_class = CupomSerializer 

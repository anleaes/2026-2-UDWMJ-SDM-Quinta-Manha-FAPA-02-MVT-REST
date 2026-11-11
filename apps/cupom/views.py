from django.shortcuts import render, redirect, get_object_or_404
from .forms import CupomForm
from .models import Cupom

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

def list_cupom(request):
    template_name = 'cupom/lista_cupom.html'
    cupom= Cupom.objects.prefetch_related('evento')
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
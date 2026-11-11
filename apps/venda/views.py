from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendaForm
from .models import Venda
from django.http import HttpResponse

def criar_venda(request):
    template_name = 'venda/criar_venda.html'
    context={}
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('venda:lista_venda')
    form = VendaForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_venda(request):
    template_name = 'venda/lista_venda.html'
    venda = Venda.objects.filter()
    context = {
        'venda': venda
    }
    return render(request, template_name, context)

def editar_venda(request, id_venda):
    template_name = ('venda/criar_venda.html')
    context = {}
    venda = get_object_or_404(Venda, id=id_venda)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('venda:lista_venda')
    form = VendaForm(instance=venda)
    context['form']=form
    return render(request, template_name, context)

def deletar_venda(request, id_venda):
    venda = Venda.objects.get(id=id_venda)
    venda.delete()
    return redirect('venda:lista_venda')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import IngressoForm
from .models import Ingresso

def criar_ingresso(request):
    template_name = 'ingresso/criar_ingresso.html'
    context = {}
    if request.method == 'POST':
        form = IngressoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('ingresso:lista_ingresso')
    form = IngressoForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_ingresso(request):
    template_name = 'ingresso/lista_ingresso.html'
    ingresso = Ingresso.objects.filter()
    context = {
        'ingresso': ingresso
    }
    return render(request, template_name, context)

def editar_ingresso(request, id_ingresso):
    template_name = 'ingresso/criar_ingresso.html'
    context = {}
    ingresso = get_object_or_404(Ingresso, id=id_ingresso)
    if request.method == 'POST':
        form = IngressoForm(request.POST, instance=ingresso)
        if form.is_valid():
            form.save()
            return redirect('ingresso:lista_ingresso')
    form = IngressoForm(instance=ingresso)
    context['form']=form
    return render(request, template_name, context)

    

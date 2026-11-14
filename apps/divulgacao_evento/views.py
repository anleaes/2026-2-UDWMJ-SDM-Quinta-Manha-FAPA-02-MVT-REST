from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import Divulgacao_EventoForm
from .models import Divulgacao_Evento

def criar_divulgacao_evento(request):
    template_name = 'divulgacao_evento/criar_divulgacao_evento.html'
    context = {}
    if request.method == 'POST':
        form = Divulgacao_EventoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('divulgacao_evento:lista_divulgacao_evento')
        else:
            context['erros_validacao'] = list(form.errors.items())
            context['form'] = Divulgacao_EventoForm(request.POST)
            return render(request, template_name, context)
    form = Divulgacao_EventoForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_divulgacao_eventos(request):
    template_name = 'divulgacao_evento/lista_divulgacao_evento.html'
    divulgacao_evento = Divulgacao_Evento.objects.filter()
    context = {
        'divulgacao_evento': divulgacao_evento
    }
    return render(request, template_name, context)

def editar_divulgacao_evento(request, id_divulgacao_evento):
    template_name = 'divulgacao_evento/criar_divulgacao_evento.html'
    context = {}
    divulgacao_evento = get_object_or_404(Divulgacao_Evento, id=id_divulgacao_evento)
    if request.method == 'POST':
        form = Divulgacao_EventoForm(request.POST, instance=divulgacao_evento)
        if form.is_valid():
            form.save()
            return redirect('divulgacao_evento:lista_divulgacao_evento')
    form = Divulgacao_EventoForm(instance=divulgacao_evento)
    context['form'] = form
    return render(request, template_name, context)

def deletar_divulgacao_evento(request, id_divulgacao_evento):
    divulgacao_evento = Divulgacao_Evento.objects.get(id=id_divulgacao_evento)
    divulgacao_evento.delete()
    return redirect('divulgacao_evento:lista_divulgacao_evento')
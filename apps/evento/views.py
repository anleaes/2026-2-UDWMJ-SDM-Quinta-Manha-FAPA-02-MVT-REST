from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from .models import Evento

def criar_evento(request):
    template_name='evento/criar_evento.html'
    context= {}

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('evento:listar_eventos')
    form = EventoForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_eventos(request):
    template_name='evento/listar_eventos.html'
    eventos = Evento.objects.filter()
    context= {
        'eventos': eventos
    }
    return render(request, template_name, context)

def editar_evento(request, id_evento):
    template_name='evento/criar_evento.html'
    context = {}
    evento = get_object_or_404(Evento, id=id_evento)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento:listar_eventos')
    form = EventoForm(instance=evento)
    context['form'] = form
    return render(request, template_name, context)

def excluir_evento(request, id_evento):
    evento = Evento.objects.get(id=id_evento)
    evento.delete()
    return redirect('evento:listar_eventos')

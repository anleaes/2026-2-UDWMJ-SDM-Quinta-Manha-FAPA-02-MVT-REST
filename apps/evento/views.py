from django.shortcuts import render, redirect
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
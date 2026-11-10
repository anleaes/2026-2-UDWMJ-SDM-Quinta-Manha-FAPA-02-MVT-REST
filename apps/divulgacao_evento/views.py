from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import Divulgacao_EventoForm

def criar_divulgacao_evento(request):
    template_name = 'divulgacao_evento/criar_divulgacao_evento.html'
    context = {}
    if request.method == 'POST':
        form = Divulgacao_EventoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return HttpResponse('Sucesso', status=200)
    form = Divulgacao_EventoForm()
    context['form'] = form
    return render(request, template_name, context)

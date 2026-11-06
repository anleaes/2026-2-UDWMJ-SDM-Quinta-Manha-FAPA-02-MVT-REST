from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Sede
from .forms import SedeForm

def criar_sede(request: HttpRequest):
    template_name = 'sede/criar_sede.html'
    context = {}

    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            # redirecionar para listar Sedes
    
    form = SedeForm()
    context['form'] = form
    return render(request, template_name, context)


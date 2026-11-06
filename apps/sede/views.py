from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Sede
from .forms import SedeForm

def criar_sede(request: HttpRequest):
    template_name = 'sede/criar_sede.html'
    context = {}

    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            obj_sede = form.save(commit=False)
            obj_sede.save()
            form.save_m2m()
            # redirecionar para listar Sedes
            return redirect('index:inicial')
            # return HttpResponse("Sucesso") # temporário

    form = SedeForm()
    context['form'] = form
    return render(request, template_name, context)


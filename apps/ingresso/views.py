from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import IngressoForm
from .models import Ingresso

def criar_ingresso(request):
    template_name = 'criar/criar_ingresso.html'
    context = {}
    if request.method == 'POST':
        form = IngressoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return HttpResponse('Sucesso', status=200)
    form = IngressoForm()
    context['form'] = form
    return render(request, template_name, context)

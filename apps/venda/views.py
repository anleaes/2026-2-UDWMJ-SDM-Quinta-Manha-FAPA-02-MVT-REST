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
            return HttpResponse('Sucesso', status=200)
    form = VendaForm()
    context['venda'] = form
    return render(request, template_name, context)
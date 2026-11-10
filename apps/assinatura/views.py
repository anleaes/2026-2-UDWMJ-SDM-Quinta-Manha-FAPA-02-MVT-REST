from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AssinaturaForm
from .models import Assinatura


def criar_assinatura(request: HttpRequest):
    template_name = 'assinatura/criar_assinatura.html'
    context = {}

    if request.method == 'POST':
        form = AssinaturaForm(request.POST)
        if form.is_valid():
            obj_assinatura = form.save(commit=False)
            obj_assinatura.save()
            form.save_m2m()
            return HttpResponse('Sucesso')

    form = AssinaturaForm()
    context = {'form': form}
    return render(request, template_name, context)


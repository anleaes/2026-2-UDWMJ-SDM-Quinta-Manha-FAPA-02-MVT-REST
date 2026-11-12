from django.shortcuts import render, redirect, get_object_or_404
from .forms import Cartao_VipForm
from .models import Cartao_Vip
from django.http import HttpResponse

def criar_cartao_vip(request):
    template_name = 'cartao_vip/criar_cartao_vip.html'
    context = {}
    if request.method == 'POST':
        form = Cartao_VipForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return HttpResponse('Sucesso', status=200)
    form = Cartao_VipForm()
    context['form'] = form
    return render(request, template_name, context)
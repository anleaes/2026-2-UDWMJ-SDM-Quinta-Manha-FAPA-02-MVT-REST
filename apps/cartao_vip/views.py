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
            return redirect('cartao_vip:lista_cartao_vip')
    form = Cartao_VipForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_cartao_vip(request):
    template_name = 'cartao_vip/lista_cartao_vip.html'
    cartao_vip = Cartao_Vip.objects.filter()
    context = {
        'cartao_vip': cartao_vip
    }
    return render(request, template_name, context)

def editar_cartao_vip(request, id_cartao_vip):
    template_name = 'cartao_vip/criar_cartao_vip.html'
    context = {}
    cartao_vip = get_object_or_404(Cartao_Vip, id=id_cartao_vip)
    if request.method == 'POST':
        form = Cartao_VipForm(request.POST, instance=cartao_vip)
        if form.is_valid():
            form.save()
            return redirect('cartao_vip:lista_cartao_vip')
    form = Cartao_VipForm(instance=cartao_vip)
    context['form'] = form
    return render(request, template_name, context)

def deletar_cartao_vip(request, id_cartao_vip):
    cartao_vip = Cartao_Vip.objects.get(id=id_cartao_vip)
    cartao_vip.delete()
    return redirect('cartao_vip:lista_cartao_vip')
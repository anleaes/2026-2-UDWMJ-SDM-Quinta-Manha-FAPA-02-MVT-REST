from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from cupom.models import Cupom
from divulgacao_evento.models import Divulgacao_Evento
from .forms import IngressoForm
from .models import Ingresso
from rest_framework import viewsets
from .serializer import IngressoSerializer
from decimal import Decimal


def calcular_preco_final(ingresso):
    if ingresso.cupom_aplicado is None:
        return ingresso.evento_divulgado.preco_base
    else:
        return (
            ingresso.evento_divulgado.preco_base * 
            (Decimal(1) - (Decimal(ingresso.cupom_aplicado.porcentagem_desconto) / Decimal(100)))
        )

def criar_ingresso(request):
    template_name = 'ingresso/criar_ingresso.html'
    context = {}
    if request.method == 'POST':
        form = IngressoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            
            if f.cupom_aplicado is not None:

                cupom = f.cupom_aplicado
                evento_valido = cupom.eventos_validos.filter(id=f.evento_divulgado.evento_id).exists()
                cupom_vencido = cupom.data_vencimento < timezone.localdate()

                if not evento_valido or cupom_vencido:
                    context['form'] = form
                    return render(request, template_name, context)

            f.preco_final = calcular_preco_final(f) 
            f.save()

            venda = f.venda
            venda.async_recalcular_preco_total()

            form.save_m2m()
            return redirect('ingresso:lista_ingresso')
        else:
            context['erros_validacao'] = list(form.errors.items())
            context['form'] = IngressoForm(request.POST)
            return render(request, template_name, context)
    form = IngressoForm()
    context['form'] = form
    return render(request, template_name, context)

def lista_ingresso(request):
    template_name = 'ingresso/lista_ingresso.html'
    ingresso = Ingresso.objects.filter()
    context = {
        'ingresso': ingresso
    }
    return render(request, template_name, context)

def editar_ingresso(request, id_ingresso):
    template_name = 'ingresso/criar_ingresso.html'
    context = {}
    ingresso = get_object_or_404(Ingresso, id=id_ingresso)
    if request.method == 'POST':
        form = IngressoForm(request.POST, instance=ingresso)
        if form.is_valid():

            ingresso.preco_final = calcular_preco_final(ingresso)
            form.save()

            venda = ingresso.venda
            venda.async_recalcular_preco_total()

            return redirect('ingresso:lista_ingresso')
        else:
            context['erros_validacao'] = list(form.errors.items())
            context['form'] = IngressoForm(request.POST)
            return render(request, template_name, context)
    form = IngressoForm(instance=ingresso)
    context['form']=form
    return render(request, template_name, context)

def deletar_ingresso(request, id_ingresso):
    ingresso = Ingresso.objects.get(id=id_ingresso)
    ingresso.delete()

    venda = ingresso.venda
    venda.async_recalcular_preco_total()

    return redirect('ingresso:lista_ingresso')

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer 
    

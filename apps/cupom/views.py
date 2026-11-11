from django.shortcuts import render
from .forms import CupomForm
from django.http import HttpResponse

def criar_cupom(request):
    template_name = 'cupom/criar_cupom.html'
    context={}

    if request.method == 'POST':
        form = CupomForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return HttpResponse('Sucesso', status=200)
    form = CupomForm()
    context['form'] = form
    return render(request, template_name, context)
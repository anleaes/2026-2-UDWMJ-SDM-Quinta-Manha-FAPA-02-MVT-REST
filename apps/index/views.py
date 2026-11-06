from django.shortcuts import render

def inicial(request):
    template_name ='index/inicial.html'
    context = {}
    return render(request, template_name, context)

from django.http import HttpRequest,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Beneficio
from .forms import BeneficioForm
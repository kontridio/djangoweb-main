from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import utulek, pes, zajemce


def index(request):
    utulky = utulek.objects.all()
    context = {
        'utulky': utulky
    }
    return render(request, 'index.html', context=context)


class UtulekListView(ListView):
    model = utulek
    context_object_name = 'utulky'
    template_name = 'utulek/utulky_list.html'


class UtulekDetailView(DetailView):
    model = utulek
    context_object_name = 'utulek'
    template_name = 'utulek/utulek_detail.html'


class PesListView(ListView):
    model = pes
    context_object_name = 'psi'
    template_name = 'pes/psi_list.html'


class PesDetailView(DetailView):
    model = pes
    context_object_name = 'pes'
    template_name = 'pes/pes_detail.html'

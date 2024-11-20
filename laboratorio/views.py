from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

from .models import Laboratorio

class LaboratorioView(ListView):
    model = Laboratorio
    template_name = "laboratorios/laboratorios.html"
    context_object_name = 'laboratorio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Página de Laboratorios'
        return context
class LaboratorioAddView(CreateView):
    model = Laboratorio
    template_name = "laboratorios/add_laboratorio.html"
    fields = ['laboratorio', 'ciudad','pais']
    success_url = reverse_lazy('laboratorio')
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    template_name = "laboratorios/upd_laboratorio.html"
    fields = ['laboratorio', 'ciudad','pais']
    success_url = reverse_lazy('laboratorio')
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = "laboratorios/del_laboratorio.html"
    fields = ['laboratorio', 'ciudad','pais']
    success_url = reverse_lazy('laboratorio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
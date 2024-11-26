from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from .forms import LaboratorioForm

from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Laboratorio
from .forms import LaboratorioForm

class LaboratorioView(ListView):
    model = Laboratorio

    template_name = "laboratorios/laboratorios.html"
    context_object_name = 'laboratorio'
    ordering = ['id']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Página de Laboratorios'
        return context
    
class LaboratorioAddView(CreateView):
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = "laboratorios/add_laboratorio.html"
    fields = ['laboratorio', 'ciudad','pais']
    success_url = reverse_lazy('laboratorio')
    
    def form_valid(self, form):
        # You can add additional custom logic here before saving the object
        laboratorio = form.save(commit=False)  # Do not save yet
        # You could modify the item object here if needed
        laboratorio.save()  # Now save the object
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Handle invalid form, perhaps log the error or add custom handling
        return super().form_invalid(form)
   
    
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
    
def add_laboratorio(request):
    
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        
        if form.is_valid():
            try:
                laboratorio = form.save(commit=False)
                laboratorio.clean() # váldamos que cumpla con las restricciones del modelo
                laboratorio.save() # guardamos los datos del modelo
                messages.success(request, "laboratorio creado correctamente.")
            
            except ValidationError as e:
                messages.error(request, e.messages)
        else:
            messages.error(request, "Error al intentar crear el laboratorio, intente nuevamente.")
        
        return render(request, "laboratorios/add_laboratorio.html", {"form": LaboratorioForm()})
    
    else:
        form = LaboratorioForm()
        return render(request, "laboratorios/add_laboratorio.html", {"form": form})
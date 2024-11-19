from django.urls import path
from . import views

urlpatterns = [
    path('laboratorio/', views.LaboratorioView.as_view(), name='laboratorio'),
    path('laboratorio/add', views.LaboratorioAddView.as_view(), name='add_laboratorio'),
    path('laboratorio/<int:pk>/update/', views.LaboratorioUpdateView.as_view(), name='upd_laboratorio'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('laboratorio/', views.LaboratorioView.as_view(), name='laboratorio'),
    path('add/laboratorio', views.add_laboratorio, name="add_laboratorio"),
    path('laboratorio/update/<int:pk>', views.LaboratorioUpdateView.as_view(), name='upd_laboratorio'),
    path('laboratorio/delete/<int:pk>', views.LaboratorioDeleteView.as_view(), name='del_laboratorio'),
]
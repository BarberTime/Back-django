# apps/empleado/urls.py
from django.urls import path
from .views import EmpleadoList, EmpleadoDetail, EmpleadoLogin, SubirFotoPerfil, EliminarFotoPerfil

urlpatterns = [
    path('api/empleados/', EmpleadoList.as_view(), name='empleados-list'),
    path('api/empleados/<uuid:id_empleado>/', EmpleadoDetail.as_view(), name='empleados-detail'),
    path('api/empleados/login/', EmpleadoLogin.as_view(), name='empleados-login'),
    path('api/empleados/<uuid:empleado_id>/subir-foto/', SubirFotoPerfil.as_view(), name='subir-foto-perfil'),
    path('api/empleados/<uuid:empleado_id>/eliminar-foto/', EliminarFotoPerfil.as_view(), name='eliminar-foto-perfil'),
]
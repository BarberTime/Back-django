from django.urls import path
from .views import RegistroAPI, LoginAPI, ListaUsuarios, EliminarUsuario, DetalleUsuario, ActualizarUsuario, VerRolAPI

urlpatterns = [
    path('api/registro/', RegistroAPI.as_view(), name='registro'),
    path('api/iniciar-sesion/', LoginAPI.as_view(), name='iniciar-sesion'),
    path('api/usuarios/', ListaUsuarios.as_view(), name='lista-usuarios'),
    path('api/usuarios/<int:pk>/', DetalleUsuario.as_view(), name='detalle-usuario'),
    path('api/usuarios/<int:pk>/actualizar/', ActualizarUsuario.as_view(), name='actualizar-usuario'),
    path('api/usuarios/<int:pk>/eliminar/', EliminarUsuario.as_view(), name='eliminar-usuario'),
    path('api/ver-rol/', VerRolAPI.as_view(), name='ver-rol'),
]
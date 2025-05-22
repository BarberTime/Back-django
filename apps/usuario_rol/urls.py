from django.urls import path
from .views import UsuarioRolList, UsuarioRolDetail, UsuarioRolUpdate, UsuarioRolDelete

urlpatterns = [
    path('api/usuario_rol/', UsuarioRolList.as_view(), name='usuario_rol-list'),
    path('api/usuario_rol/<uuid:id_usuario_rol>/', UsuarioRolDetail.as_view(), name='usuario_rol-detail'),
    path('api/usuario_rol/<uuid:id_usuario_rol>/actualizar/', UsuarioRolUpdate.as_view(), name='usuario_rol-update'),
    path('api/usuario_rol/<uuid:id_usuario_rol>/eliminar/', UsuarioRolDelete.as_view(), name='usuario_rol-delete'),
]
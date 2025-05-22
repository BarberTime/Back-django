from django.urls import path
from .views import RolList, RolDetail, RolUpdate, RolDelete

urlpatterns = [
    path('api/rol/', RolList.as_view(), name='rol-list'),
    path('api/rol/<uuid:id_rol>/', RolDetail.as_view(), name='rol-detail'),
    path('api/rol/<uuid:id_rol>/actualizar/', RolUpdate.as_view(), name='rol-update'),
    path('api/rol/<uuid:id_rol>/eliminar/', RolDelete.as_view(), name='rol-delete'),
]
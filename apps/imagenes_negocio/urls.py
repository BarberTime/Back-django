from django.urls import path
from .views import ImagenesNegocioList, ImagenesNegocioDetail, ImagenesNegocioUpdate, ImagenesNegocioDelete

urlpatterns = [
    path('api/imagen_negocio/', ImagenesNegocioList.as_view(), name='imagen_negocio-list'),
    path('api/imagen_negocio/<int:id_imagen>/', ImagenesNegocioDetail.as_view(), name='imagen_negocio-detail'),
    path('api/imagen_negocio/<int:id_imagen>/actualizar/', ImagenesNegocioUpdate.as_view(), name='imagen_negocio-update'),
    path('api/imagen_negocio/<int:id_imagen>/eliminar/', ImagenesNegocioDelete.as_view(), name='imagen_negocio-delete'),
]
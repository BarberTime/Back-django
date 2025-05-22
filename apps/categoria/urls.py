from django.urls import path
from .views import CategoriaList, CategoriaDetail, CategoriaUpdate, CategoriaDelete

urlpatterns = [
    path('api/v1/categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('api/v1/categorias/<uuid:id_categoria>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('api/v1/categorias/<uuid:id_categoria>/update/', CategoriaUpdate.as_view(), name='categoria-update'),
    path('api/v1/categorias/<uuid:id_categoria>/delete/', CategoriaDelete.as_view(), name='categoria-delete'),
]

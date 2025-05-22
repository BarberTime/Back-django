from django.urls import path
from .views import ReservaList, ReservaDetail, ReservaUpdate, ReservaDelete

urlpatterns = [
    path('api/reserva/', ReservaList.as_view(), name='reserva-list'),
    path('api/reserva/<uuid:id_reserva>/', ReservaDetail.as_view(), name='reserva-detail'),
    path('api/reserva/<uuid:id_reserva>/actualizar/', ReservaUpdate.as_view(), name='reserva-update'),
    path('api/reserva/<uuid:id_reserva>/eliminar/', ReservaDelete.as_view(), name='reserva-delete'),
]
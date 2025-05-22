from django.urls import path
from .views import PagoList, PagoDetail, PagoUpdate, PagoDelete

urlpatterns = [
    path('api/pago/', PagoList.as_view(), name='pago-list'),
    path('api/pago/<uuid:id_pago>/', PagoDetail.as_view(), name='pago-detail'),
    path('api/pago/<uuid:id_pago>/actualizar/', PagoUpdate.as_view(), name='pago-update'),
    path('api/pago/<uuid:id_pago>/eliminar/', PagoDelete.as_view(), name='pago-delete'),
]
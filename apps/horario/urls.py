from django.urls import path
from .views import HorarioList, HorarioDetail, HorarioUpdate, HorarioDelete

urlpatterns = [
    path('api/horario/', HorarioList.as_view(), name='horario-list'),
    path('api/horario/<uuid:id_horario>/', HorarioDetail.as_view(), name='horario-detail'),
    path('api/horario/<uuid:id_horario>/actualizar/', HorarioUpdate.as_view(), name='horario-update'),
    path('api/horario/<uuid:id_horario>/eliminar/', HorarioDelete.as_view(), name='horario-delete'),
]

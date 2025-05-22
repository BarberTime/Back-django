from django.urls import path
from .views import PlanListCreateView, PlanDetailView, SuscripcionListCreateView, SuscripcionDetailView

urlpatterns = [
    # Planes
    path('api/plan/', PlanListCreateView.as_view(), name='plan-list'),
    path('api/plan/<uuid:id>/', PlanDetailView.as_view(), name='plan-detail'),
    
    # Suscripciones
    path('api/suscripcion/', SuscripcionListCreateView.as_view(), name='suscripcion-list'),
    path('api/suscripcion/<uuid:id>/', SuscripcionDetailView.as_view(), name='suscripcion-detail'),
]

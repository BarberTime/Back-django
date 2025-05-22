from rest_framework import serializers
from .models import Plan, Suscripcion
from apps.negocio.serializers import NegocioSerializer

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'nombre', 'descripcion', 'precio_mensual', 'duracion_dias', 'max_reservas', 
                 'max_servicios', 'max_horarios', 'soporte_prioritario', 'estadisticas_avanzadas',
                 'fecha_creacion', 'activo']
        read_only_fields = ['id', 'fecha_creacion']

class SuscripcionSerializer(serializers.ModelSerializer):
    negocio = NegocioSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    dias_restantes = serializers.SerializerMethodField()

    class Meta:
        model = Suscripcion
        fields = ['id', 'negocio', 'plan', 'fecha_inicio', 'fecha_expiracion', 'estado',
                 'fecha_ultimo_pago', 'fecha_proximo_pago', 'dias_restantes']
        read_only_fields = ['id', 'fecha_inicio', 'fecha_ultimo_pago', 'fecha_proximo_pago']

    def get_dias_restantes(self, obj):
        return obj.dias_restantes()

    def validate(self, data):
        if 'fecha_expiracion' in data and data['fecha_expiracion'] <= timezone.now():
            raise serializers.ValidationError('La fecha de expiración debe ser posterior a la fecha actual')
        return data

    def create(self, validated_data):
        negocio = validated_data['negocio']
        plan = validated_data['plan']
        
        if Suscripcion.objects.filter(negocio=negocio, estado='ACTIVA').exists():
            raise serializers.ValidationError('Ya existe una suscripción activa para este negocio')
            
        suscripcion = Suscripcion.objects.create(
            negocio=negocio,
            plan=plan,
            fecha_expiracion=timezone.now() + timezone.timedelta(days=plan.duracion_dias)
        )
        return suscripcion

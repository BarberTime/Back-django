# apps/empleado/models.py
from django.db import models
from django.contrib.auth.models import User
from apps.negocio.models import Negocio
import uuid


class Empleado(models.Model):
    id_empleado = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    experiencia_anios = models.IntegerField()
    foto_perfil = models.ImageField(upload_to='empleados/fotos/', null=True, blank=True)
    fecha_contratacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.rol_id:
            try:
                self.rol = Rol.objects.get(nombre='Empleado')
            except Rol.DoesNotExist:
                self.rol = Rol.objects.create(nombre='Empleado')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.username} - {self.especialidad}"
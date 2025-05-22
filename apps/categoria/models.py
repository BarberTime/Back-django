from django.db import models
import uuid

class Categoria(models.Model):
    id_categoria = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
    
    def __str__(self):
        return self.nombre

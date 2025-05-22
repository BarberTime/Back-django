def get_negocio_folder(instance, filename):
    # Reemplazar espacios y caracteres especiales con guiones
    nombre_negocio = instance.nombre.lower()
    nombre_negocio = ''.join(c if c.isalnum() else '-' for c in nombre_negocio)
    
    # Obtener el tipo de archivo
    extension = filename.split('.')[-1]
    
    # Generar la ruta
    if isinstance(instance, Negocio):
        return f'barberia/negocios/{nombre_negocio}/logo.{extension}'
    elif hasattr(instance, 'negocio'):
        return f'barberia/negocios/{nombre_negocio}/servicios/{filename}'
    return f'barberia/negocios/{nombre_negocio}/{filename}'

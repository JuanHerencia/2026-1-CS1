# ejercicio1.py  integración
from modulo_a import obtener_usuario
from modulo_b import calcular_anio_nacimiento

usuario = obtener_usuario()
print(calcular_anio_nacimiento(usuario, 2026))  # TypeError
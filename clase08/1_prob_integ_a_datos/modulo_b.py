# modulo_b.py - Consume datos (asume que edad es int)
def calcular_anio_nacimiento(usuario, anio_actual):
    return anio_actual - usuario["edad"]  # Error: str - int

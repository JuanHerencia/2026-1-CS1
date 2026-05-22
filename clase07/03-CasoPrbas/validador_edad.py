# validador_edad.py
def es_edad_valida(edad: int) -> bool:
    """Retorna True si edad está entre 18 y 65 (inclusive)"""
    return 18 <= edad <= 65
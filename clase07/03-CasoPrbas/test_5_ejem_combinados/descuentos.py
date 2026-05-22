# descuentos.py
def calcular_precio_descuento(categoria: str, precio_base: float) -> float:
    """
    Categorías:
    - 'normal': sin descuento
    - 'vip': 20% descuento
    - 'staff': 50% descuento
    """
    if categoria == 'normal':
        return precio_base
    elif categoria == 'vip':
        return precio_base * 0.8
    elif categoria == 'staff':
        return precio_base * 0.5
    else:
        raise ValueError(f"Categoría desconocida: {categoria}")
'''
Contratos de Interfaces: Precondiciones y Postcondiciones 
Situación real (historia): Un equipo implementó una función 
calcular_cuota_prestamo() sin documentar sus precondiciones.
Un desarrollador llamó a la función con una tasa de interés 
negativa (error en validación upstream) y la función devolvió
un valor sin sentido que causó pérdidas contables. La 
investigación reveló que la función asumía que la tasa era
positiva, pero esa suposición estaba solo en la mente del 
autor original. 
'''
# Ejemplo (sin contrato - PELIGROSO):
def calcular_cuota_prestamo(monto, tasa_anual, plazos_meses): 
    # ¿Qué pasa si monto <= 0? ¿tasa_anual negativa? ¿plazos_meses = 0? 
    tasa_mensual = tasa_anual / 12 / 100 
    factor = (1 + tasa_mensual) ** plazos_meses 
    return monto * (tasa_mensual * factor) / (factor - 1) 

# Solución - Con contrato explícito
def calcular_cuota_prestamo( 
    monto: float,
    tasa_anual_porcentaje: float, 
    plazos_meses: int 
) -> float: 

    """ 
    Calcula la cuota mensual fija de un préstamo (sistema francés). 
    Precondiciones (el caller debe garantizar): 
        - monto > 0 
        - tasa_anual_porcentaje >= 0 
        - plazos_meses >= 1 

    Postcondiciones (quien llama puede confiar en): 
        - El resultado será >= 0 
        - Si tasa_anual_porcentaje == 0, resultado == monto / plazos_meses 
        - Si plazos_meses == 1, resultado == monto + interés 

    Ejemplos: 
        >>> calcular_cuota_prestamo(10000, 12, 12)  # 12% anual, 12 meses 
        888.49  # aprox, incluye interés mensual 

    Raises: 
        ValueError: Si alguna precondición no se cumple 
    """ 

    # Validación explícita de precondiciones 
    if monto <= 0: 
        raise ValueError(f"El monto debe ser positivo. Recibido: {monto}") 
    if tasa_anual_porcentaje < 0: 
        raise ValueError(f"La tasa no puede ser negativa. Recibida: {tasa_anual_porcentaje}") 
    if plazos_meses < 1: 
        raise ValueError(f"Los plazos deben ser >= 1. Recibido: {plazos_meses}") 

    # Caso especial: tasa 0 
    if tasa_anual_porcentaje == 0: 
        resultado = monto / plazos_meses 
        # Verificar postcondición (opcional, modo debug) 
        assert resultado >= 0, "Postcondición violada: resultado negativo con tasa 0" 
        return resultado 

    tasa_mensual = tasa_anual_porcentaje / 12 / 100 
    factor = (1 + tasa_mensual) ** plazos_meses 
    resultado = monto * (tasa_mensual * factor) / (factor - 1) 

    # Validación de postcondiciones (modo desarrollo) 
    assert resultado >= 0, f"Postcondición violada: resultado negativo {resultado}" 
    return resultado 

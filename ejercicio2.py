'''
Situación real: Una función getApp() en un proyecto alcanzó una 
complejidad ciclomática de 25, cuando el umbral recomendado es 9. 
Esto significa que hay 25 caminos independientes a través del 
código, haciendo casi imposible probar todos los escenarios. 

Síntomas de alta complejidad: 
  Múltiples if-else anidados 
  Dificultad para entender qué hace la función 
  Alta probabilidad de regresiones al modificar 
  Pruebas unitarias extremadamente complejas 
-------------------------------------------------
Solución: Refactorizar para reducir la complejidad
'''
# Complejidad ciclomática: 8+ (mala) 
def procesar_pago(metodo, monto, usuario, pais, es_recurrente): 
    if metodo == "tarjeta": 
        if pais == "PE": 
            if es_recurrente: 
                resultado = procesar_suscripcion_visa(monto, usuario) 
            else: 
                if monto > 1000: 
                    resultado = procesar_pago_visa_con_autenticacion(monto, usuario) 
                else: 
                    resultado = procesar_pago_visa_simple(monto, usuario) 
        elif pais == "MX": 
            # lógica similar con condicionales anidados... 
            pass 
    elif metodo == "paypal": 
        # más condicionales anidados... 
        pass 
    elif metodo == "transferencia": 
        # más condicionales... 
        pass 
    return resultado 

# Solución
def obtener_estrategis_pago(metodo, pais, es_recurrente):
    # Tabla de decisiones en lugar de condicionales
    estrategia = {
        ("tarjeta", "PE", True): estrategisSubscripcionVISA(),
        ("tarjeta", "PE", False): estrategisPagoVISA(),
        ("tarjeta", "MX", True): estrategisSubscripcionMastercard(),
        ("Paypal", "*", True): estrategisPayPal(),
    }
    key = (metodo, pais, es_recurrente)
    return estrategia.get(key, EstrategiaDefault()) # EstrategiaDefault() es cuando no encuentra la clave


def procesar_pago(metodo, monto, usuario, pais, es_recurrente): 
    estrategia = obtener_estrategis_pago(metodo, pais, es_recurrente)
    return estrategia_procesar(monto, usuario)


contador_errores = 0

def registrar_error(mensaje):
    global contador_errores
    contador_errores += 1
    print(f"Error: {mensaje}")

def obtener_contador():
    return contador_errores
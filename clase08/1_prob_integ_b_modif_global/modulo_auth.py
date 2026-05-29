from modulo_log import contador_errores  # OJO: importa el valor actual, no referencia

def autenticar(usuario):
    # Simula verificación
    if usuario == "admin":
        return True
    else:
        from modulo_log import registrar_error
        registrar_error("Auth fallida")
        return False
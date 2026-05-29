# Módulo A - desarrollado en aislamiento
def modulo_a():
    return {"status": "ok", "value": "42"}

# Módulo B - desarrollado en aislamiento, supone que value es entero
def modulo_b(data):
    return data["value"] * 2  # espera int, recibe str → error

# Módulo C - usa B, supone que B devuelve string
def modulo_c():
    resultado_b = modulo_b(modulo_a())
    return f"Resultado: {resultado_b}"

# ========== INTEGRACIÓN BIG BANG (al final del proyecto) ==========
if __name__ == "__main__":
    # Todo junto por primera vez
    try:
        print(modulo_b())
    except TypeError as e:
        print(f"💥 BIG BANG EXPLOTA: {e}")
        print("Múltiples fallos aparecen a la vez, difíciles de aislar:")
        print(" - Módulo A devuelve string, módulo B espera int")
        print(" - Módulo B devuelve int, módulo C espera string")
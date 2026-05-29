# ========== stubs (simulaciones temporales) ==========
# stub para capa de datos (aún no implementada)
def obtener_precio_stub(producto):
    return 100.0  # precio fijo para pruebas

def obtener_impuesto_stub(ubicacion):
    return 0.18  # IGV 18% fijo

# ========== capa media (real) ==========
def calcular_total(productos, ubicacion, obtener_precio, obtener_impuesto):
    subtotal = sum(obtener_precio(p) for p in productos)
    impuesto = subtotal * obtener_impuesto(ubicacion)
    return subtotal + impuesto

# ========== capa superior (real) - se integra primero ==========
def mostrar_resumen(productos, ubicacion):
    total = calcular_total(productos, ubicacion, obtener_precio_stub, obtener_impuesto_stub)
    print(f"Resumen del pedido:")
    print(f"  Productos: {productos}")
    print(f"  Total: ${total:.2f}")
    return total

# ========== integración top-down ==========
if __name__ == "__main__":
    # Probamos la capa superior + stubs
    mostrar_resumen(["laptop", "mouse"], "CL")  # funciona sin datos reales
    
    # Luego, cuando la capa de datos esté lista, reemplazamos stubs:
    # def obtener_precio_real(producto): ...
    # def obtener_impuesto_real(ubicacion): ...
    # y solo cambiamos las funciones pasadas.
# ========== capa inferior (datos) - real ==========
def obtener_precio_real(producto):
    precios = {"laptop": 800, "mouse": 25, "teclado": 60} # de la bd
    return precios.get(producto, 0)

def obtener_impuesto_real(ubicacion):
    impuestos = {"CL": 0.19, "PE": 0.18, "MX": 0.16}  # de la bd
    return impuestos.get(ubicacion, 0.21)

# ========== capa media (lógica) - real ==========
def calcular_total(productos, ubicacion, obtener_precio, obtener_impuesto):
    subtotal = sum(obtener_precio(p) for p in productos)
    impuesto = subtotal * obtener_impuesto(ubicacion)
    return subtotal + impuesto

# ========== driver (programa de prueba temporal) ==========
# simula la capa superior que aún no existe
def driver_prueba():
    productos = ["laptop", "mouse"]
    total = calcular_total(productos, "CL", obtener_precio_real, obtener_impuesto_real)
    print(f"[Driver] Total calculado desde capas bajas: ${total:.2f}")
    return total

# ========== integración bottom-up ==========
if __name__ == "__main__":
    # Probamos capa inferior + capa media con un driver
    driver_prueba()
    
    # Luego, cuando la capa superior (UI) esté lista, integramos:
    # def mostrar_resumen(productos, ubicacion):
    #     total = calcular_total(productos, ubicacion, obtener_precio_real, obtener_impuesto_real)
    #     print(...)
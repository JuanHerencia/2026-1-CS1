# test_integracion.py
import unittest

# módulos reales del sistema
def obtener_precio(p):
    return {"laptop": 800, "mouse": 25}.get(p, 0)

def obtener_impuesto(u):
    return {"CL": 0.19}.get(u, 0.21)

def calcular_total(productos, ubicacion):
    subtotal = sum(obtener_precio(p) for p in productos)
    return subtotal * (1 + obtener_impuesto(ubicacion))

def mostrar_resumen(productos, ubicacion):
    total = calcular_total(productos, ubicacion)
    return f"Total: ${total:.2f}"

# Pruebas de integración que corren en cada commit
class TestIntegracionContinua(unittest.TestCase):
    def test_flujo_completo(self):
        resultado = mostrar_resumen(["laptop", "mouse"], "CL")
        self.assertEqual(resultado, "Total: $981.75")  # 825 * 1.19

    def test_integracion_capas(self):
        total = calcular_total(["laptop"], "CL")
        self.assertAlmostEqual(total, 800 * 1.19)

# Simulación de pipeline CI
if __name__ == "__main__":
    print("Ejecutando suite de integración continua...")
    unittest.main()
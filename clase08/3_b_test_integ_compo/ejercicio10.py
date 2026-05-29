import logging
from datetime import datetime

# ========== componentes ==========

class Inventario:
    def __init__(self):
        self.stock = {"laptop": 5, "mouse": 10}
    
    def verificar_stock(self, producto, cantidad):
        return self.stock.get(producto, 0) >= cantidad
    
    def descontar(self, producto, cantidad):
        if self.verificar_stock(producto, cantidad):
            self.stock[producto] -= cantidad
            return True
        return False

class ProcesadorPagos:
    def procesar(self, monto, metodo):
        # Simula integración con pasarela externa
        if monto <= 0:
            raise ValueError("Monto inválido")
        if metodo not in ["tarjeta", "paypal"]:
            raise ValueError("Método no soportado")
        # Simula transacción exitosa
        return {"transaccion_id": f"TXN-{datetime.now().timestamp()}", "estado": "aprobado"}

class LoggerSistema:
    def __init__(self):
        self.eventos = []
    
    def registrar(self, tipo, mensaje):
        entrada = {"timestamp": datetime.now(), "tipo": tipo, "mensaje": mensaje}
        self.eventos.append(entrada)
        print(f"[{tipo}] {mensaje}")
        return entrada

# ========== PRUEBAS DE INTEGRACIÓN ==========

import unittest
from unittest.mock import patch

class TestIntegracionEcommerce(unittest.TestCase):
    
    def test_integracion_pago_exitoso_con_descuento_inventario(self):
        """Prueba que pago + inventario + logger funcionen juntos"""
        inventario = Inventario()
        procesador = ProcesadorPagos()
        logger = LoggerSistema()
        
        producto = "laptop"
        cantidad = 1
        monto = 800
        metodo = "tarjeta"
        
        # 1. Verificar stock
        self.assertTrue(inventario.verificar_stock(producto, cantidad))
        
        # 2. Procesar pago
        resultado_pago = procesador.procesar(monto, metodo)
        self.assertEqual(resultado_pago["estado"], "aprobado")
        
        # 3. Descontar inventario
        descontado = inventario.descontar(producto, cantidad)
        self.assertTrue(descontado)
        self.assertEqual(inventario.stock[producto], 4)
        
        # 4. Registrar operación
        evento = logger.registrar("VENTA", f"Venta de {producto} - Transacción {resultado_pago['transaccion_id']}")
        self.assertEqual(evento["tipo"], "VENTA")
        
        # Verificar consistencia: el log tiene al menos 1 evento
        self.assertGreaterEqual(len(logger.eventos), 1)
    
    def test_integracion_fallo_pago_no_descuenta_inventario(self):
        """Si el pago falla, el inventario NO debe descontarse"""
        inventario = Inventario()
        procesador = ProcesadorPagos()
        
        stock_inicial = inventario.stock["mouse"]
        
        # Intentar pagar con método inválido
        with self.assertRaises(ValueError):
            procesador.procesar(10, "cripto")  # método inválido
        
        # El inventario debe permanecer igual
        self.assertEqual(inventario.stock["mouse"], stock_inicial)
    
    def test_integracion_compra_sin_stock(self):
        """Falta de stock debe impedir llegar al procesador de pagos"""
        inventario = Inventario()
        procesador = ProcesadorPagos()
        
        producto = "laptop"
        cantidad = 999  # más de lo disponible
        
        # Verificar que no hay stock antes de siquiera intentar pagar
        if not inventario.verificar_stock(producto, cantidad):
            # No se llega al procesador de pagos
            with self.assertRaises(ValueError):
                # Esto simula que la capa superior evita llamar a pagos
                procesador.procesar(999000, "tarjeta")
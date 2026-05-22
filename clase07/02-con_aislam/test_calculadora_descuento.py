# test_calculadora_descuento.py
import pytest
from unittest.mock import Mock
from calculadora_descuento import CalculadoraDescuento

def test_calcular_precio_final_con_descuento():
    # Creamos un doble de prueba (mock) que simula el servicio real
    servicio_mock = Mock()
    servicio_mock.consultar_descuento.return_value = 20   # 20% descuento

    # Inyectamos el mock en lugar del servicio real
    calc = CalculadoraDescuento(servicio_mock)

    precio_final = calc.calcular_precio_final(user_id=123, precio_base=100)

    assert precio_final == 80   # 100 - 20%
    # Verificamos que el mock fue llamado correctamente
    servicio_mock.consultar_descuento.assert_called_once_with(123)
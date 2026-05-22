# pip install pytest
import pytest
from descuentos import calcular_precio_descuento

# ---- PARTICIONES DE EQUIVALENCIA ----
def test_particion_normal():
    assert calcular_precio_descuento('normal', 100) == 100

def test_particion_vip():
    assert calcular_precio_descuento('vip', 100) == 80

def test_particion_staff():
    assert calcular_precio_descuento('staff', 100) == 50

def test_particion_categoria_desconocida():
    with pytest.raises(ValueError):
        calcular_precio_descuento('gold', 100)

# ---- VALORES LÍMITE (para precio_base, si tuviera límites) ----
# En este caso no aplica directamente, pero si precio_base tuviera límites (ej: no negativo)
def test_precio_base_limite_cero():
    assert calcular_precio_descuento('vip', 0) == 0

# ---- CAMINO FELIZ ----
def test_happy_path_vip_precio_normal():
    assert calcular_precio_descuento('vip', 200) == 160

def test_happy_path_staff_precio_pequeno():
    assert calcular_precio_descuento('staff', 10) == 5

# ---- CASOS NEGATIVOS ----
def test_categoria_vacia():
    with pytest.raises(ValueError):
        calcular_precio_descuento('', 100)

def test_precio_base_negativo():
    # La función actual lo permite, pero quizás no debería
    assert calcular_precio_descuento('vip', -100) == -80  # Comportamiento actual

def test_categoria_none():
    with pytest.raises(ValueError):
        calcular_precio_descuento(None, 100)
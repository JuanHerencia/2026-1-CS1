# test_validador_negativo.py
import pytest
from validador_edad import es_edad_valida

def test_edad_negativa():
    assert es_edad_valida(-5) == False

def test_edad_cero():
    assert es_edad_valida(0) == False

def test_edad_muy_grande():
    assert es_edad_valida(150) == False

def test_edad_con_float():
    # Si la función solo acepta int, esto puede lanzar TypeError
    with pytest.raises(TypeError):
        es_edad_valida(18.5)
    
    
def test_edad_con_string():
    with pytest.raises(TypeError):
        es_edad_valida("veinte")
# test_validador_equivalencia.py
from validador_edad import es_edad_valida

def test_edad_muy_baja():
    assert es_edad_valida(15) == False   # Representante clase <18

def test_edad_valida():
    assert es_edad_valida(30) == True    # Representante clase 18-65

def test_edad_muy_alta():
    assert es_edad_valida(70) == False   # Representante clase >65
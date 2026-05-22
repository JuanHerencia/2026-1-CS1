# test_validador_limites.py
from validador_edad import es_edad_valida

def test_limite_inferior():
    assert es_edad_valida(17) == False   # justo antes
    assert es_edad_valida(18) == True    # justo en el límite
    assert es_edad_valida(19) == True    # justo después

def test_limite_superior():
    assert es_edad_valida(64) == True    # justo antes
    assert es_edad_valida(65) == True    # justo en el límite
    assert es_edad_valida(66) == False   # justo después
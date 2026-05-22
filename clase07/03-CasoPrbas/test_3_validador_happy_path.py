# test_validador_happy_path.py
from validador_edad import es_edad_valida

def test_edad_adulto_joven():
    assert es_edad_valida(25) == True

def test_edad_adulto_medio():
    assert es_edad_valida(40) == True

def test_edad_casi_jubilacion():
    assert es_edad_valida(60) == True
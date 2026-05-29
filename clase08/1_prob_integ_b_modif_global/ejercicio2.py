# ejercicio2.py  integración
from modulo_auth import autenticar
from modulo_log import contador_errores, obtener_contador

print("Estado inicial contador:", contador_errores)  # 0
autenticar("invitado")
print("Contador según variable importada:", contador_errores)  # 0 (efecto colateral no visto)
print("Contador según función:", obtener_contador())         # 1 (el efecto existe)
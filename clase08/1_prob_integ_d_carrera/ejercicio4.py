# ejercicio4.py
import threading
from modulo_deposito import depositar
from modulo_retiro import retirar
from global_file import saldo_compartido

hilos = []
for _ in range(10000):
    h1 = threading.Thread(target=retirar, args=(10,))
    h2 = threading.Thread(target=depositar, args=(10,))
    hilos.extend([h1, h2])
    h1.start()
    h2.start()

for h in hilos:
    h.join()

print(f"Saldo final esperado: 100000, obtenido: {saldo_compartido}")
# Probablemente no sea 1000 por condiciones de carrera
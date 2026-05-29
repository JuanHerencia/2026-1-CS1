# modulo_retiro.py
from global_file import saldo_compartido
def retirar(monto):
    global saldo_compartido
    if saldo_compartido >= monto:
        # Simula operación no atómica
        temp = saldo_compartido
        temp -= monto
        saldo_compartido = temp
    else:
        print("Fondos insuficientes")
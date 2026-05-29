# modulo_deposito.py
from global_file import saldo_compartido
def depositar(monto):
    global saldo_compartido
    temp = saldo_compartido
    temp += monto
    saldo_compartido = temp
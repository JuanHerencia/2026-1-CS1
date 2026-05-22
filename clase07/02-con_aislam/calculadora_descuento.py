# calculadora_descuento.py (versión con inyección)
class CalculadoraDescuento:
    def __init__(self, servicio_descuento):
        self.servicio = servicio_descuento   # Dependencia inyectada

    def calcular_precio_final(self, user_id, precio_base):
        descuento = self.servicio.consultar_descuento(user_id)
        return precio_base * (1 - descuento / 100)
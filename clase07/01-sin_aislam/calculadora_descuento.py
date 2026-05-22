from servicio_descuento import ServicioDescuento

class CalculadoraDescuento:
    def __init__(self):
        self.servicio = ServicioDescuento()

    def calcular_precio_final(self, user_id, precio_base):
        descuento = self.servicio.consultar_descuento(user_id)
        return precio_base * (1 - descuento / 100)
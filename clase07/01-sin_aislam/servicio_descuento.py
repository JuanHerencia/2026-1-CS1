import requests

class ServicioDescuento:
    def consultar_descuento(self, user_id):
        # Dependencia real: llamada HTTP
        resp = requests.get(f"https://api.ejemplo.com/users/{user_id}/descuento")
        return resp.json()["porcentaje"]
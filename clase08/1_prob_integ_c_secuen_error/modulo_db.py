# modulo_db.py
class Database:
    def __init__(self):
        self.conectado = False

    def conectar(self):
        print("Conectando...")
        self.conectado = True

    def consultar(self, sql):
        if not self.conectado:
            raise RuntimeError("No se puede consultar sin conectar")
        return f"Resultado de: {sql}"
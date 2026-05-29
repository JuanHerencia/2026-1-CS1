from modulo_db import Database

def generar_reporte(db, consulta):
    # Olvidaron llamar a conectar() antes
    return db.consultar(consulta)
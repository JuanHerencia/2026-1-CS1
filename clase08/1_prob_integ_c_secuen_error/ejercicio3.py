from modulo_db import Database
from modulo_reportes import generar_reporte

db = Database()
print(generar_reporte(db, "SELECT * FROM users"))  # RuntimeError
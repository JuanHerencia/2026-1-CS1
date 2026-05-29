# ========== componentes individuales ==========

# componente 1: validador de email
class ValidadorEmail:
    def validar(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido")
        return True

# componente 2: repositorio de usuarios (simula DB)
class RepositorioUsuarios:
    def __init__(self):
        self.usuarios = {}
    
    def guardar(self, email, nombre):
        if email in self.usuarios:
            raise ValueError("Usuario ya existe")
        self.usuarios[email] = {"nombre": nombre, "activo": True}
        return True
    
    def existe(self, email):
        return email in self.usuarios

# componente 3: servicio de notificaciones
class ServicioNotificaciones:
    def enviar_bienvenida(self, email, nombre):
        # Simula envío de email
        print(f"📧 Enviando bienvenida a {nombre} <{email}>")
        return True

# ========== PRUEBA DE INTEGRACIÓN ==========
# Verifica que los 3 componentes trabajen juntos correctamente

import unittest

class TestIntegracionRegistroUsuario(unittest.TestCase):
    
    def setUp(self):
        # Crear instancias reales (no mocks para integración)
        self.validador = ValidadorEmail()
        self.repo = RepositorioUsuarios()
        self.notificador = ServicioNotificaciones()
    
    def test_flujo_registro_completo(self):
        """Prueba que validador + repo + notificador funcionen integrados"""
        email = "ana@ejemplo.com"
        nombre = "Ana"
        
        # 1. Validar email
        es_valido = self.validador.validar(email)
        self.assertTrue(es_valido)
        
        # 2. Guardar en repositorio
        guardado = self.repo.guardar(email, nombre)
        self.assertTrue(guardado)
        self.assertTrue(self.repo.existe(email))
        
        # 3. Enviar notificación
        enviado = self.notificador.enviar_bienvenida(email, nombre)
        self.assertTrue(enviado)
    
    def test_integracion_rechaza_email_duplicado(self):
        """Prueba la interacción entre repo y validador para duplicados"""
        email = "pedro@ejemplo.com"
        
        # Primero guardar un usuario
        self.repo.guardar(email, "Pedro")
        
        # Intentar guardar el mismo email (la integración debe fallar)
        with self.assertRaises(ValueError):
            self.repo.guardar(email, "Pedro2")
    
    def test_integracion_validador_evita_datos_invalidos(self):
        """El validador debe evitar que datos inválidos lleguen al repo"""
        email_invalido = "correo-sin-arroba"
        
        # El validador debe lanzar error antes de que el repo intente guardar
        with self.assertRaises(ValueError):
            self.validador.validar(email_invalido)
            # Esta línea nunca se ejecuta si el validador falla
            self.repo.guardar(email_invalido, "Invalido")

if __name__ == "__main__":
    unittest.main()
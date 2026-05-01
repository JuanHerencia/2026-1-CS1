'''
Situación real (historia): Un proyecto Python tenía 3 maneras
diferentes de estructurar un archivo de módulo: 
  Estilo A: imports → constantes → funciones → clase principal 
  Estilo B: clase principal → funciones auxiliares → constantes → imports 
  Estilo C: todo mezclado sin orden aparente 

Un desarrollador nuevo invirtió 2 horas buscando dónde se definía
una constante porque en el archivo A estaba al inicio, en el B al
final. El equipo adoptó un estándar (inspirado en PEP 8 y Google 
Python Style Guide) y el tiempo de búsqueda se redujo a segundos. 
'''
# Código recomendado
"""Módulo para gestión de usuarios del sistema. 
Este módulo contiene las clases y funciones necesarias para 
el registro, autenticación y perfilado de usuarios. 
""" 
# 1. Imports estándar de la biblioteca Python 
import hashlib 
import logging 
from datetime import datetime 
from typing import Optional, List 

# 2. Imports de terceros (librerías externas) 
import jwt 
from sqlalchemy import Column, String, Integer 

# 3. Imports locales del proyecto 
from config.settings import SECRET_KEY 
from database.session import get_session 

# 4. Constantes de módulo (nivel de archivo) 
MAX_INTENTOS_FALLIDOS = 5 
TIEMPO_BLOQUEO_MINUTOS = 30 
ROL_ADMIN = "admin" 
ROL_USUARIO = "usuario" 

# 5. Clases principales (ordenadas por jerarquía) 
class Usuario: 
    """Representa un usuario del sistema.""" 
    def __init__(self, nombre: str, email: str): 
        """Para crear el objeto Usuario"""
        self.nombre = nombre 
        self.email = email 
        self._intentos_fallidos = 0 

    # Métodos públicos primero 
    def autenticar(self, password: str) -> bool: 
        """Verifica si la contraseña es correcta.""" 
        return self._verificar_password(password) 

    def cambiar_rol(self, nuevo_rol: str) -> None: 
        """Cambia el rol del usuario (requiere permisos de admin).""" 
        if nuevo_rol not in [ROL_ADMIN, ROL_USUARIO]: 
            raise ValueError(f"Rol inválido: {nuevo_rol}") 
        self.rol = nuevo_rol 

    # Métodos privados después (prefijo _) 
    def _verificar_password(self, password: str) -> bool: 
        """Método interno de verificación.""" 
        return hashlib.sha256(password.encode()).hexdigest() == self._password_hash 

    # Propiedades al final 
    @property 
    def esta_bloqueado(self) -> bool: 
        return self._intentos_fallidos >= MAX_INTENTOS_FALLIDOS 

# 6. Funciones auxiliares de módulo (si no pertenecen a una clase) 
def crear_usuario_por_defecto(nombre: str) -> Usuario: 
    """Crea un usuario con configuración por defecto.""" 
    return Usuario(nombre, f"{nombre}@ejemplo.com") 

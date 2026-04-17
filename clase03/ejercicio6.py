'''
Situación real: Una plataforma SaaS necesita gestionar diferentes
tipos de usuarios (Cliente, Administrador, Moderador, Vendedor)
todos con atributos comunes . 
'''
# Ejemplo (reutilización por herencia): 
from abc import ABC, abstractmethod 
from datetime import datetime 
from typing import List, Optional 

# ============================================ 
# Clase base reusable (contiene lo común) 
# ============================================ 

class BaseUser(ABC): 
    """ 
    Clase base abstracta para todos los usuarios del sistema. 
    Contiene atributos y métodos comunes a TODOS los tipos de usuario. 
    """ 

     

    def __init__(self, user_id: str, email: str, created_at: datetime = None): 

        self._user_id = user_id 

        self._email = email 

        self._created_at = created_at or datetime.now() 

        self._is_active = True 

        self._login_attempts = 0 

     

    # Métodos comunes reutilizados por todas las subclases 

    def get_user_id(self) -> str: 

        return self._user_id 

     

    def get_email(self) -> str: 

        return self._email 

     

    def is_active(self) -> bool: 

        return self._is_active 

     

    def deactivate(self) -> None: 

        self._is_active = False 

     

    def record_failed_login(self) -> None: 

        self._login_attempts += 1 

        if self._login_attempts >= 5: 

            self.deactivate() 

     

    def reset_login_attempts(self) -> None: 

        self._login_attempts = 0 

     

    # Método abstracto: cada subclase implementa su propia lógica 

    @abstractmethod 

    def get_permissions(self) -> List[str]: 

        """Retorna la lista de permisos para este tipo de usuario""" 

        pass 

     

    @abstractmethod 

    def get_dashboard_config(self) -> dict: 

        """Retorna la configuración del dashboard específica del rol""" 

        pass 

 

 

# ============================================ 

# Subclases: solo definen lo que las hace únicas 

# ============================================ 

class Customer(BaseUser): 

    """Cliente regular de la plataforma""" 

     

    def __init__(self, user_id: str, email: str, shipping_address: str = None): 

        super().__init__(user_id, email) 

        self.shipping_address = shipping_address 

        self.cart = [] 

     

    def get_permissions(self) -> List[str]: 

        # Los clientes solo pueden comprar y ver su perfil 

        return ["view_products", "add_to_cart", "checkout", "view_orders"] 

     

    def get_dashboard_config(self) -> dict: 

        return { 

            "sections": ["Recent Orders", "Recommendations", "Wishlist"], 

            "theme": "light" 

        } 

     

    # Métodos específicos de Customer 

    def add_to_cart(self, product_id: str) -> None: 

        self.cart.append(product_id) 

 

 

class Admin(BaseUser): 

    """Administrador del sistema (máximos privilegios)""" 

     

    def __init__(self, user_id: str, email: str, admin_level: int = 1): 

        super().__init__(user_id, email) 

        self.admin_level = admin_level 

     

    def get_permissions(self) -> List[str]: 

        # Los administradores tienen todos los permisos 

        return ["*"]  # Wildcard para "todos los permisos" 

     

    def get_dashboard_config(self) -> dict: 

        return { 

            "sections": ["Analytics", "User Management", "System Logs", "Reports"], 

            "theme": "dark", 

            "show_technical_metrics": True 

        } 

     

    # Métodos específicos de Admin 

    def ban_user(self, user_id: str) -> None: 

        print(f"Usuario {user_id} ha sido baneado por {self._user_id}") 

     

    def view_system_metrics(self) -> dict: 

        return {"cpu": 45, "memory": 62, "requests": 15420} 

 

 

class Vendor(BaseUser): 

    """Vendedor en el marketplace""" 

     

    def __init__(self, user_id: str, email: str, store_name: str): 

        super().__init__(user_id, email) 

        self.store_name = store_name 

        self.products = [] 

     

    def get_permissions(self) -> List[str]: 

        return ["manage_products", "view_inventory", "process_orders", "view_sales"] 

     

    def get_dashboard_config(self) -> dict: 

        return { 

            "sections": ["Sales Summary", "Inventory Status", "Customer Reviews"], 

            "theme": "light" 

        } 

     

    # Métodos específicos de Vendor 

    def add_product(self, product_name: str, price: float) -> None: 

        self.products.append({"name": product_name, "price": price}) 

        print(f"Producto '{product_name}' añadido a la tienda {self.store_name}") 

 

 

# ============================================ 

# Uso: código que trabaja con cualquier tipo de usuario 

# ============================================ 

class AuthenticationService: 

    """Servicio que maneja cualquier tipo de usuario de forma polimórfica""" 

     

    def __init__(self): 

        self._users: dict[str, BaseUser] = {} 

     

    def register_user(self, user: BaseUser) -> None: 

        """Registra CUALQUIER tipo de usuario (polimorfismo)""" 

        self._users[user.get_user_id()] = user 

        print(f"Usuario {user.get_user_id()} registrado como {type(user).__name__}") 

     

    def get_user_permissions(self, user_id: str) -> List[str]: 

        """Obtiene permisos sin importar el tipo de usuario""" 

        user = self._users.get(user_id) 

        if user: 

            return user.get_permissions() 

        return [] 

     

    def get_dashboard(self, user_id: str) -> dict: 

        """Cada usuario obtiene su dashboard personalizado""" 

        user = self._users.get(user_id) 

        if user: 

            return user.get_dashboard_config() 

        return {"error": "User not found"} 

 

 

# Demostración 

if __name__ == "__main__": 

    auth = AuthenticationService() 

     

    # Todos se registran con el mismo método 

    auth.register_user(Customer("C001", "cliente@email.com", "Av. Siempre Viva 123")) 

    auth.register_user(Admin("A001", "admin@empresa.com", admin_level=3)) 

    auth.register_user(Vendor("V001", "vendedor@tienda.com", "Tech Store")) 

     

    # Cada usuario obtiene su dashboard específico (¡mismo método, diferentes resultados!) 

    print(auth.get_dashboard("C001"))  # {"sections": ["Recent Orders", ...], "theme": "light"} 

    print(auth.get_dashboard("A001"))  # {"sections": ["Analytics", "User Management", ...], "theme": "dark"} 
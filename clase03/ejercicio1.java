// Ejercio 1
/*
 Facturador accede a Cliente y luego directamente a Direccion 
para obtener la ciudad. Si la estructura de Direccion cambia (ej. 
se añade un idioma o se separa código postal), Facturador se rompe. 
*/

public class Facturador { 
    public void imprimirFactura(Cliente cliente) { 
        // Depende de la estructura interna de Direccion 
        String ciudad = cliente.getDireccion().getCiudad();  
        System.out.println("Ciudad: " + ciudad); 
    } 
} 

 
# Alta complejidad: todo junto 
def procesar_nomina(empleados, empresa, mes): 
    conexion = crear_conexion_bd() 
    # lógica de validación de empleados 
    for emp in empleados: 
        if emp['activo'] and emp['sueldo'] > 0: 
            # cálculo de sueldo 
            sueldo_base = emp['sueldo'] 
            if empresa['pais'] == 'PE': 
                impuesto = sueldo_base * 0.08 
                afp = sueldo_base * 0.10 
            elif empresa['pais'] == 'MX': 
                impuesto = sueldo_base * 0.15 
                afp = sueldo_base * 0.05 

            # más lógica de bonos, descuentos, etc. 
            # también actualiza BD y genera PDF 
            conexion.execute(f"UPDATE ... SET sueldo_neto = {sueldo_base - impuesto - afp}") 
            generar_pdf(emp['nombre'], sueldo_base - impuesto - afp) 
1# Datos iniciales
datos = {
    "producto": "Zapatillas Air Max",
    "talla": 42,
    "color": "Rojo",
    "stock": 20
}

# Funcion que modifica  claves del producto(diccionario)
def modificar_clave():
    # Mostrar el estado inicial del producto
    print("Producto en existencias:", datos)
    
    # Solicitar clave para modificar
    clave_modificar = input("Ingresa la clave cuyo valor deseas modificar: ")
    if clave_modificar in datos: # Si la clave existe, realizar la modificacion
        nuevo_valor = input(f"Ingresa el nuevo valor para '{clave_modificar}': ")
        datos[clave_modificar] = nuevo_valor # Asignar el nuevo valor
        print("Informacion del producto actualizada:", datos) # Mostrar mensaje de producto actualizado
    else:
        print(f"La clave '{clave_modificar}' no existe en la informacion del producto.") # Mostrar mensaje, que clave no existe
        print("Informacion del producto sin cambios:", datos) # Mantener la informacion del producto sin cambios

# Funcion que elimina claves del producto(diccionario)
def eliminar_clave():
    # Solicitar clave para eliminar
    clave_eliminar = input("Ingresa la clave que deseas eliminar: ")
    if clave_eliminar in datos: # Si la clave existe, la elimina
        valor_eliminado = datos.pop(clave_eliminar) # Utilizar .pop para eliminar
        print(f"Clave '{clave_eliminar}' eliminada. Valor eliminado: {valor_eliminado}") #Mostrar mensaje de que la clave fue eliminada
        print("Informacion del producto actualizada", datos)
    else:
        print(f"La clave '{clave_eliminar}' no existe en la informacion del producto.") # Mostrar mensaje, que clave no existe
        print("Informacion del producto sin cambios:", datos) # Mantener la informacion del producto sin cambios


# Funcion para el programa principal
def menu_principal():
    opcion = 0  
    while opcion != 3:  # El bucle continua hasta que la opcion sea 3
        print("Opciones:")
        print("1. Modificar una clave")
        print("2. Eliminar una clave")
        print("3. Salir")

        # Capturamos la opcion del usuario
        opcion = int(input("Selecciona una opcion del menu (1/2/3): "))
        
        # Procesamos la opcion ingresada
        if opcion == 1:
            modificar_clave()  # Llamar a la funcion para modificar
        elif opcion == 2:
            eliminar_clave()  # Llamar a la funcion para eliminar
        elif opcion == 3:
            print("Saliendo del programa.") # Salir del programa
        else:
            print("Opcion invalida. Por favor, intenta nuevamente.") # Mostrar mensaje de error,1 si se digita otro numero diferente de 1,2 o 3

# Llamamos a la funcion principal para iniciar el programa
menu_principal()

# Referencias
# Pdf del profesor
# https://ellibrodepython.com/diccionarios-en-python
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

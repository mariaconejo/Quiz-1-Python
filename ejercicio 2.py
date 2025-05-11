# Funcion para mostrar la lista de nombres
def mostrar_lista_nombres():
    nombres = ["Maria", "Oscar", "Ericka", "Sharon"]
    print("Lista de nombres:")
    for nombre in nombres:  # Recorre la lista de nombres
        print(f"- {nombre}")

# Funcion principal del programa
def menu_interactivo():
    opcion = 0  # Inicializamos opcion diferente a 3
    while opcion != 3:  # El bucle se ejecutara mientras la opcion sea distinta de 3
        print("Menu Interactivo:")
        print("1. Mostrar un mensaje")
        print("2. Mostrar una lista de nombres")
        print("3. Salir del programa")

        # Capturar la opcion del usuario
        opcion = int(input("Selecciona una opcion del menu (1/2/3): "))  # Convertir str en int

        # Procesar la opcion ingresada
        if opcion == 1:
             print("¡Sigue adelante! Los grandes logros comienzan con pequeños pasos y grandes esfuerzos.")
        elif opcion == 2:
            mostrar_lista_nombres() #Llamar a la funcion mostrar_lista_nombres()
        elif opcion == 3:
            print("Gracias por usar el programa. ¡Hasta pronto!")  # Salir del programa
        else:
            print("Opcion no valida. Por favor, intenta nuevamente.")  # Mostrar mensaje de error, si se digita otro numero diferente de 1,2 o 3

# Llamamos a la funcion principal para iniciar el programa
menu_interactivo()

# Referencias
# Pdf del profesor
# https://ellibrodepython.com/listas-en-python
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists


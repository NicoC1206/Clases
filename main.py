from pantalla import mostrar_titulo, titulo_menu, menu_opciones
from Calculos import es_navegable, alertar_viento_peligroso, obtener_temperatura_limite_traje, mostrar_advertencia_marejada

def menu():
    mostrar_titulo
    titulo_menu()
    altura_ola = float(input("Ingrese la altura de las olas en metros\n:"))
    viento = int(input("Ingrese la velocidad del viento en nudos\n:"))
    while True:
        menu_opciones()
        opcion = input("Seleccione una opción")
        if opcion == "1":
            apto = es_navegable(altura_ola)
            if apto == True:
                print("Se puede hacer WingFoil")
            else:
                print("No se puede hacer WingFoil")
        elif opcion == "2":
            alertar_viento_peligroso(viento)
        elif opcion == "3":
            tem = obtener_temperatura_limite_traje
            print(f"Bajo los {tem} es obligatorio usar traje  4/3mm ")
        elif opcion == "4":
            mostrar_advertencia_marejada
        elif opcion == "5":
            altura_ola = float(input("Ingrese la altura de las olas en metros\n:"))
            viento = int(input("Ingrese la velocidad del viento en nudos\n:"))
            print("Datos actualizados")
        elif opcion == "6":
            print("Saliendo del sistema")
            break
        else:
            print("Opción no valida")
if __name__ == "__main__":
    menu()
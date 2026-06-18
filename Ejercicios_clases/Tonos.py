import winsound
import time
print("Sintetizado de microtonos")
maximo_microtonos = 50
microtonos_libres = 50
microtonos_activos =0
ejecutando = True

while ejecutando:
    print("\n === Panel de microtonos")
    print("1.- Ver cuántos microtonos quedan libres")
    print("2.- Activar microtonos")
    print("3.- Devolver microtonos")
    print("4.- Monitorear el estado actual delos microtonos")
    print("5.- Salir")

    opción = int(input("Elige una opción\n:"))
    if opción == 1:
        print(f"\n[INFO] Tienes {microtonos_libres} microtonos disponibles para usar")
    elif opción == 2:
        if microtonos_libres == 0:
            print("No tienes más microtonos disponibles")
        else:
            try:
                cantidad = int(input("¿Cuántos microtonos quieres usar?"))
                if cantidad <= 0:
                    print("Error tienes que activar al menos 1 microtono")
                elif cantidad > microtonos_libres:
                    print(f"No hay tantos microtonos, máximo disponible {microtonos_libres}")
                else:
                    microtonos_libres -= cantidad 
                    microtonos_activos += cantidad
                    #for i in range(1,cantidad + 1):
                    #   print(f"Activando microtono {i} de {cantidad}")
                    #   winsound.Beep(440, 300)
                    #   time.sleep(0.5)
                    
                    cancion = [
                        (311,250), (311,250), (311,500),
                        (311,250), (311,250), (311,500),
                        (311,250), (370,250), (277,250), (293,250),
                        (311,1000),
                        (320,250), (320,250), (320,500), (320,250),
                        (320,250), (311,500), (311,250), (311,125), (311,125),
                        (311,250), (293,250), (293,250), (311,255),
                        (277,500), (429, 500)

                    ]
                    for i in range(len(cancion)):
                        frecuencia = cancion[i][0]
                        duracion = cancion[i][1]
                        winsound.Beep(frecuencia, duracion)
                        time.sleep(0.05)
            except ValueError:
                print("Error, por favor ingresa un número válido")
else:
    print("Error, opción no válida, por favor elige una opción del 1 al 5")
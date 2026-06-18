'''
Enunciado del Ejercicio: "Sistema de Control de Estado de Servidores"
1. Datos que debe manejar el sistema
El sistema trabaja con una colección de servidores. Esta colección debe existir desde que el programa inicia y estar disponible durante toda la ejecución. Cada vez que se agrega un servidor, se incorpora a esa colección como un nuevo elemento.

Cada servidor se representa como un conjunto de campos asociados: nombre, uptime, carga y un indicador de si está critico o no. La siguiente tabla resume los campos de cada registro:

CampoQué representaRestricciones de validación"nombre"Identificador único del servidorNo vacío ni solo espacios en blanco."uptime"Días continuos encendidoNúmero entero mayor que cero."carga"Porcentaje de uso de CPU (1.0–100.0)Número decimal entre 1.0 y 100.0 (incluidos)."critico"¿Superó el umbral seguro de operación?False al registrar. El sistema lo asigna automáticamente. Su valor puede cambiar a True cuando se ejecute la opción 4 (Actualizar estados), según la carga del servidor.



Cada diccionario se guarda dentro de una lista. La lista es la colección general; los diccionarios son los servidores individuales dentro de ella. El programa comienza con la lista vacía y la va llenando a medida que se agregan registros.

2. Lo que debe hacer el sistema
El sistema se controla desde un menú que aparece en pantalla cada vez que el usuario termina una acción. El usuario elige una opción numérica, el programa ejecuta la tarea correspondiente y vuelve a mostrar el menú. Esto se repite hasta que el usuario elige salir.

El menú tiene seis opciones:

Plaintext



========== MENÚ PRINCIPAL ==========
1. Agregar servidor
2. Buscar servidor
3. Eliminar servidor
4. Actualizar estados
5. Mostrar servidores
6. Salir
=====================================
 
Función de interfaz 1: Muestra las opciones en pantalla (no recibe nada, no retorna nada).
Función de interfaz 2: Lee y retorna la opción elegida (no recibe nada, retorna el número validado).
'''
#serian dos archivos, el main y la pantalla, el main se encarga de ejecutar el programa
#la pantalla se encarga de mostrar el menu y el titulo del programa, 
# el main importa las funciones del menu y el titulo desde la pantalla para usarlas en su ejecución.

from Pantalla_P4 import menu, titulo

servidores = [] #lista vacía para almacenar los servidores

titulo()

def main(): #función principal del programa
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Opción 1: Agregar servidor")
            server_name = input("Ingrese el nombre del servidor: ")
            uptime = int(input("Ingrese el uptime del servidor (en días): "))
            carga = float(input("Ingrese la carga del servidor (en porcentaje): "))
            critico = False
            servidor = {
                "nombre": server_name,
                "uptime": uptime,
                "carga": carga,
                "critico": critico
            }   
            servidores.append(servidor)
            print(f"Servidor '{server_name}' agregado exitosamente.")
            # Lógica para agregar servidor
        elif opcion == "2":
            print("Opción 2: Buscar servidor")
            server_name = input("Ingrese el nombre del servidor a buscar: ")
            for servidor in servidores:
                if servidor["nombre"] == server_name:
                    print(f"Nombre: {servidor['nombre']}, Uptime: {servidor['uptime']} días, Carga: {servidor['carga']}%, Crítico: {servidor['critico']}")
                    break
            else:
                print(f"Servidor '{server_name}' no encontrado.")
            # Lógica para buscar servidor
        elif opcion == "3":
            print("Opción 3: Eliminar servidor")
            server_name = input("Ingrese el nombre del servidor a eliminar: ")
            for i, servidor in enumerate(servidores):
                if servidor["nombre"] == server_name:
                    del servidores[i]
                    print(f"Servidor '{server_name}' eliminado exitosamente.")
                    break
            else:
                print(f"Servidor '{server_name}' no encontrado.")
            # Lógica para eliminar servidor
        elif opcion == "4":
            print("Opción 4: Actualizar estados")
            for servidor in servidores:
                if servidor["carga"] > 80.0:
                    servidor["critico"] = True
                else:
                    servidor["critico"] = False
            print("Estados de los servidores actualizados según la carga.")
            # Lógica para actualizar estados
        elif opcion == "5":
            print("Opción 5: Mostrar servidores")
            if not servidores:
                print("No hay servidores registrados.")
            else:
                for servidor in servidores:
                    print(f"Nombre: {servidor['nombre']}, Uptime: {servidor['uptime']} días, Carga: {servidor['carga']}%, Crítico: {servidor['critico']}")
            # Lógica para mostrar servidores
        elif opcion == "6":
            print("Opción 6: Salir")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
if __name__ == "__main__": #interruptor para ejecutar el programa
    main()

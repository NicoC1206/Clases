'''
Errores que fui registrando:
Para llamar a la libreria es "Nombre (puede ser cualquier nombre):(dos puntos) {empleado(libreria)["departamento"](Sección de la libreria)} (se cierran llaves de la libreria)
'''

from Pantalla import titulo, menu

lista_empleados = []

titulo()

def main():
    while True:
        menu()
        op = input("Escoge una opción: ")
        if op == "1":
            nombre = input("Nombre completo del empleado: ").strip()
            departamento = input("Área donde trabaja: ").strip()
            horas_semana = int(input("Horas trabajadas por semana: "))
            salario = float(input("Sueldo mensual en CLP: "))
            if salario <= 0:
                print("Por favor, ingrese un número positivo mayor a cero")
            while True:
                activo = input("¿Está actualmente contratado?: ")
                if activo == "si":
                    activo = True
                    break
                elif activo == "no":
                    activo = False
                    break
                else:
                    print("Opción invalida, debe contestar con si o no")
            empleado = {
                "nombre": nombre,
                "departamento": departamento,
                "horas_semanales": horas_semana,
                "salario": salario,
                "activo": activo
            }
            lista_empleados.append(empleado)
            print("Empleado registrado")
        elif op == "2":
            empleado_buscado = input("Nombre del empleado que desea buscar: ")
            if len(lista_empleados) == 0:
                print("No hay empleados registrados")
            else:
                encontrado = False
                for empleado in lista_empleados:
                    if empleado["nombre"].lower() == empleado_buscado.lower():
                        print(f"Nombre: {empleado["nombre"]}, Departamento: {empleado["departamento"]}, Horas semanales: {empleado["horas_semanales"]}, Salario: {empleado["salario"]}, Contrato: {empleado["activo"]} ")
                        encontrado = True
                if not encontrado:
                    print("No se encontró el empleado con ese nombre")
        elif op == "3":
            empleado_eliminado = input("Nombre del empleado que desea eliminar: ")
            if len(lista_empleados) == 0:
                print("No hay empleados registrados")
            else:
                for empleado in lista_empleados:
                    if empleado["nombre"].lower() == empleado_eliminado.lower():
                        lista_empleados.remove(empleado)
                        print(f"El empleado {empleado_eliminado} fue eliminado con exito")
                    else:
                        print("No se encontró el empleado con ese nombre")
        elif op == "4":
            actualizados = 0
            for empleado in lista_empleados:
                if empleado["horas_semanales"] > 45 and empleado["activo"] == True:
                    empleado["activo"] = False #se le termina el contrato al wey
                    actualizados += 1
            print(f"Se actualizaron {actualizados} empleados por sobrecarga.")
        elif op == "5":
            for empleado in lista_empleados:
                if empleado["activo"]:
                    print(f"Nombre: {empleado["nombre"]}, Departamento: {empleado["departamento"]}, Horas semanales: {empleado["horas_semanales"]}, Salario: {empleado["salario"]}, Contrato: {empleado["activo"]} ")
        elif op == "6":
            print("Saliendo del Sistema de control de empleados")
            break
        else:
            print("Opción no válida, por favor vuelta a intentar")
if __name__ == "__main__":
    main()
        
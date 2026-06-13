import funciones as fun


def main():
    print("=== Inicio del programa de registro de vehiculos ===")
    #LLamada a función sin parametros y sin retorno
    fun.mostrar_busqueda()
    #LLamada a función con parametros y sin retorno
    print("Inserción de elementos al vehiculo")
    fun.insertar_datos("nic@gmail.com",80)
    #LLamada a función sin parametros y con retorno
    diccionario_modificado = fun.actualizar_datos() #se coloca de esta manera porque se actualizan y retornan datos
    print("Actualización del diccionario, tras modificación")
    print(diccionario_modificado)
    #LLamada a función con parametros y con retorno
    print("Eliminar datos")
    eliminado = fun.eliminar_datos(0)
    print("=== Estado final del diccionario ===")
    print(fun.vehiculo)

if __name__ == "__main__":
    main()

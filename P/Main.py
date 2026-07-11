from funciones import (
    leer_opcion,
    copias_genero,
    busqueda_multa,
    actualizar_multa,
    validar_codigo,
    validar_texto,
    validar_ano,
    validar_novedad,
    validar_entero_positivo,
    validar_entero_no_negativo,
    agregar_libro,
    eliminar_libro
)


def main():
    libros = {
        'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
        'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
        'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
        'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
        'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
        'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
    }
    
    prestamos = {
        'L001': [500, 4],
        'L002': [700, 0],    
        'L003': [300, 10],
        'L004': [400, 2],
        'L005': [600, 1],
        'L006': [350, 6],
    }

    ejecutando = True
    while ejecutando:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Copias por género")
        print("2. Búsqueda de libros por rango de multa")
        print("3. Actualizar multa de libro")
        print("4. Agregar libro")
        print("5. Eliminar libro")
        print("6. Salir")
        print("=====================================")
        opcion = leer_opcion()

        if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            copias_genero(genero, libros, prestamos)
        elif opcion == 2:
            while True:
                try:
                    multa_min = int(input("Ingrese multa mínima: "))
                    multa_max = int(input("Ingrese multa máxima: "))
                    if multa_min >= 0 and multa_max >= 0 and multa_max >= multa_min:
                        break  
                    else:
                        print("Los valores deben ser positivos y el mínimo menor o igual al máximo.")
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            busqueda_multa(multa_min, multa_max, libros, prestamos)
        elif opcion == 3:
            procesar_otro = 's'
            while procesar_otro.lower() == 's':
                cod = input("Ingrese código del libro: ")
                try:
                    n_multa = int(input("Ingrese nueva multa: "))
                    if n_multa > 0:
                        if actualizar_multa(cod, n_multa, prestamos, libros):
                            print("Multa actualizada")
                        else:
                            print("El código no existe")
                    else:
                        print("La multa debe ser un entero positivo.")
                except ValueError:
                    print("Multa inválida (debe ser un número entero).")
                
                procesar_otro = input("¿Desea actualizar otra multa (s/n)?: ")
                
        elif opcion == 4:
            cod = input("Ingrese código del libro: ")
            tit = input("Ingrese título: ")
            aut = input("Ingrese autor: ")
            gen = input("Ingrese género: ")
            anio = input("Ingrese año de publicación: ")
            edit = input("Ingrese editorial: ")
            nov = input("¿Es novedad? (s/n): ")
            
            try:
                multa = int(input("Ingrese precio de multa: "))
                copias = int(input("Ingrese copias disponibles: "))
            except ValueError:
                print("Los valores numéricos deben ser enteros válidos.")
                continue  
            if (validar_codigo(cod, libros) and 
                validar_texto(tit) and 
                validar_texto(aut) and 
                validar_texto(gen) and 
                validar_ano(anio) and 
                validar_texto(edit) and 
                validar_novedad(nov) and
                validar_entero_positivo(multa) and 
                validar_entero_no_negativo(copias)):

                if agregar_libro(cod, tit, aut, gen, anio, edit, nov, multa, copias, libros, prestamos):
                    print("Libro agregado")
                else:
                    print("El código ya existe")
            else:
                print("Error: Uno o más datos no cumplen con las validaciones requeridas.")
        elif opcion == 5:
            cod = input("Ingrese código del libro a eliminar: ")
            if eliminar_libro(cod, libros, prestamos):
                print("Libro eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            ejecutando = False  
        else:
            print("Debe seleccionar una opción válida")

if __name__ == "__main__":
    main()
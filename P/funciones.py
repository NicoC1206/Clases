

def validar_codigo(codigo, libros):
    if not codigo or codigo.strip() == "":
        return False

    if codigo.upper() in libros:
        return False 
        
    return True

def validar_texto(texto):
    if not texto or texto.strip() == "":
        return False
    return True

def validar_ano(ano):
    try:
        ano_int = int(ano)
        if ano_int > 0:
            return True
        return False
    except ValueError:
        return False

def validar_novedad(es_novedad):

    if not es_novedad or es_novedad.strip() == "":
        return False

    valor = es_novedad.strip().lower()
    if valor in ['s', 'n']:
        return True
    return False

def validar_entero_positivo(valor):
    try:
        valor_int = int(valor)
        if valor_int > 0:
            return True
        return False
    except ValueError:
        return False

def validar_entero_no_negativo(valor):
    try:
        valor_int = int(valor)
        if valor_int >= 0:
            return True
        return False
    except ValueError:
        return False

def leer_opcion():

    try:
        opcion = int(input("Ingrese opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            return -1  
    except ValueError:
        return -1

def copias_genero(genero_buscar, libros, prestamos):
    total_copias = 0
    
    for cod_libro, datos in libros.items():
        genero_libro = datos[2]  
        
        if genero_libro.lower() == genero_buscar.lower():
            if cod_libro in prestamos:
                total_copias += prestamos[cod_libro][1]
                
    print(f"El total de copias disponibles es: {total_copias}")

def busqueda_multa(multa_min, multa_max, libros, prestamos):
    resultados = []
    for cod_libro, datos_p in prestamos.items():
        precio_multa = datos_p[0] 
        copias = datos_p[1]     
        

        if multa_min <= precio_multa <= multa_max and copias > 0:

            if cod_libro in libros:
                titulo = libros[cod_libro][0]
                formato_string = f"{titulo}--{cod_libro}"
                resultados.append(formato_string)
    if len(resultados) == 0:
        print("No hay libros en ese rango de multa.")
    else:
        resultados.sort()
        print(f"Los libros encontrados son: {resultados}")

def buscar_codigo(codigo, diccionario):
    return codigo.upper() in diccionario


def actualizar_multa(codigo, nueva_multa, prestamos, libros):
    if buscar_codigo(codigo, libros):
        prestamos[codigo.upper()][0] = nueva_multa
        return True
    return False

def agregar_libro(codigo, titulo, autor, genero, año, editorial, es_novedad, 
                  precio_multa, copias_disponibles, libros, prestamos):
    cod_upper = codigo.upper()
    if cod_upper in libros:
        return False 
    año_int = int(año)
    es_novedad_bool = True if es_novedad.strip().lower() == 's' else False

    libros[cod_upper] = [titulo, autor, genero, año_int, editorial, es_novedad_bool]
    prestamos[cod_upper] = [int(precio_multa), int(copias_disponibles)]
    return True

def eliminar_libro(codigo, libros, prestamos):
    if buscar_codigo(codigo, libros):
        cod_upper = codigo.upper()
        libros.pop(cod_upper)
        prestamos.pop(cod_upper)
        return True
    return False

def validar_entero_no_negativo(valor):
    try:
        valor_int = int(valor)
        return valor_int >= 0
    except ValueError:
        return False


def agregar_libro(codigo, titulo, autor, genero, año, editorial, es_novedad, 
                  precio_multa, copias_disponibles, libros, prestamos):
    codigo = codigo.upper()
    
    if buscar_codigo(codigo, libros):
        return False
    año_int = int(año)
    precio_multa_int = int(precio_multa)
    copias_int = int(copias_disponibles)

    libros[codigo] = [titulo, autor, genero, año_int, editorial, es_novedad]
    prestamos[codigo] = [precio_multa_int, copias_int]
    
    return True

def eliminar_libro(codigo, libros, prestamos):
    codigo = codigo.upper()
    
    if buscar_codigo(codigo, libros):
        del libros[codigo]
        del prestamos[codigo]
        return True
    return False
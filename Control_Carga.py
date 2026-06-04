print("Control de carga")
total_equipaje = 0

while True:
    try: 
        nombre = input("Ingrese su nombre y apellido:\n")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            raise ValueError("Error al ingresar datos, por favor ingrese su nombre solo con letras")
    except ValueError as e:
        print(e)
while True:
    try:    
        rut = input("Ingrese su rut(sin puntos, solo con guión) \nEjemplo: 12345678-9:  ")
        if rut.replace("-","").isalnum() and len(rut) == 10:
            break
        else:
            raise ValueError("Error al ingresar datos, Por favor ingrese su rut de esta forma: 12345678-9")
    except ValueError as e:
        print(e)    
while True:
    try:    
        vuelo = input("Ingrese el número de vuelo:\n")
        if int(vuelo.isdigit()) > 0 :
            break
        else:
            raise ValueError("Error al ingresar datos, Por favor ingrese su vuelo solo con números enteros y postivos")
    except ValueError as e:
        print(e)

while True:
    total_equipaje = input("¿Cuántos equipajes desea registrar?")
    try:
        total_equipaje = int(total_equipaje)
        if total_equipaje > 0:
            break
        elif total_equipaje == 0:
            raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("Error al ingresar datos, debe ser un número, entero y positivo")

ticket = nombre[0]+rut[0:2]+vuelo[0:2]
peso_permitido = 0
peso_sobrecarga = 0

for i in range(total_equipaje):
    while True:
        peso_equipaje = input(f"Ingrese el peso del equipaje N°{(i+1)}: ")
        try:
            peso_equipaje = int(peso_equipaje)
            if peso_equipaje > 0:
                break
            elif peso_equipaje == 0:
                raise ValueError
            else:
                raise ValueError
        
        except ValueError:
            print("¡Error de pesaje! Ingresa un número entero positivo para el peso.")
    ticket = nombre[0]+str(i+1)+rut[0:2]+vuelo[0:2]+str(peso_equipaje*5)

    if peso_equipaje <= 10:
        peso_permitido = peso_permitido + 1
    elif peso_equipaje > 10:
        peso_sobrecarga = peso_sobrecarga + 1


    print(f"Código de Ticket: {ticket}")
    print(f"Peso del Equipaje (kg): {peso_equipaje}")

print(f"¡El avión transportará {peso_permitido} equipajes en Cabina e {peso_sobrecarga} equipajes en Bodega! ¡Manifiesto de carga listo!")



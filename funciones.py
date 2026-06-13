#creación de diccionario
vehiculo = {
    "marca":"Peugeot", #si son : son datos base
    "modelo":"Landtrek",
    #largo x ancho x alto
    "dimensiones":[550,180,180],
    "papeles_al_dia": True
}
#1.- Fun sin parametros/ sin retorno
def mostrar_busqueda():
    print("---BUSQUEDA---")
    print("nombre", vehiculo["marca"]," ",vehiculo["modelo"])
    print("Largo del vehiculo", vehiculo["dimensiones"][0])
    print("-"*10)

#2.- Fun con parametros y sin retorno
def insertar_datos(mail_propietario, tamano_rueda):
    vehiculo["mail_propietario"] = mail_propietario
    vehiculo["dimensiones"].append(tamano_rueda)
    print(f"Datos insertados: {mail_propietario} dimension rueda: {tamano_rueda}")
#3.- Fun sin parametros y con retorno
def actualizar_datos():
    vehiculo["papeles_al_dia"] = False #si es un = le ingreso datos, para actualizar
    vehiculo["dimensiones"][1] = 185
    return vehiculo
#4.- Fun con parametros y con retorno
def eliminar_datos(largo_vehiculo):
    if "papeles_al_dia" in vehiculo:
        del vehiculo["papeles_al_dia"]
    largo = vehiculo["dimensiones"].pop(largo_vehiculo)
    return largo

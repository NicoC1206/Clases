#función con parametros y con retorno
def es_navegable(altura):
    return altura >=1.5
'''

'''

#función con parametros y sin retorno
def alertar_viento_peligroso(nudos):
    if nudos >= 20:
        print("[ALERTA]: Viento peligroso, peligro de corriente")
    else:
        print("Condiciones de viento dentro del limite")
#Función sin parametros y con retorno
def obtener_temperatura_limite_traje():
    temperatura_limite = 14
    return temperatura_limite
#funcion sin parametros y sin retorno
def mostrar_advertencia_marejada():
    print(" ")
    print("-"*10)
    print("AVISO DE LA ARMADA: MAREJADA ACTIVAS")
    print("-"*10)
    print(" ")
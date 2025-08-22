# Actualización de valores
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]
coordenadas[0]["latitud"] = 9.9355431


def iterarDiccionario(lista):
    for diccionario in lista:
        linea = ", ".join([f"{clave} - {valor}" for clave, valor in diccionario.items()])
        print(linea)


def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])


def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)

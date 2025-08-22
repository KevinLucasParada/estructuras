# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Kevin" 
nombre = "Kevin"

print("Hola,", nombre)      # con coma
print("Hola " + nombre)     # con +

# 3. Imprimir "Hola!" 
numero = 156

print("Hola", numero, "!")          # con coma
print("Hola " + str(numero) + "!")  # con + y conversión

# 4. Imprimir "Me encanta comer tacos y Comida China" 
comida1 = "tacos"
comida2 = "Comida China"

print("¡Me encanta comer {} y {}!".format(comida1, comida2))  # con .format()
print(f"¡Me encanta comer {comida1} y {comida2}!")            # con f-string

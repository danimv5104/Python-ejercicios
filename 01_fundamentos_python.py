# Variables y Tipos de Datos

# Guardamos un texto (String)
nombre = "Leonardo"

# Guardamos un número entero (Integer)
edad = 16

# Guardamos un número decimal (Float)
estatura = 1.98

# Tu primera pregunta de lógica y deducción:
# Imagina que ejecutamos estas dos líneas de código en Python:

x = 10
y = 5

x = y

"""
Mi deducción es que teniendo en cuenta que la variable no es constante, el valor se sobreescribe
por lo tanto x toma el valor de y, es decir, x=5. Por lo tanto, si imprimimos x, el resultado será 5.
"""
# ---------------------------------------------------------------------
# Intercambio de Valores y Reasignación
a = 1
b = 2

# Queremos intercammbiar sus valores usando una variable temporal
temp = a
a = b
b = temp

# siguiente pregunta de lógica:
# Siguiendo paso a paso la ejecución del programa (de arriba hacia abajo):

temp = a
a = b
b = temp


"""
Pregunta:
Al terminar esas tres operaciones, ¿cuáles son los valores finales de a y de b? ¿Por qué fue necesario utilizar la variable temp en lugar de hacer simplemente a = b y b = a?#

Mi respuesta:los valores de ambos terminan teniendo el mismo valor de temp, debido a que el valor de temp es a, luego cuando a tiene el valor de b y b tiene el mismo valor de temp que es a, es un circulo cambiante pero todos con el mismo valor. La razon de usar temp o en si el valor temporal es para llenar un vacio, es decir, si en caso de que el valor de alguno no se renderice o sea hipotetico permite generar...bueno de aqui no se expllicarlo mejor. pero tengo la idea 

La respuesta ideal:
Cuando ejecutamos el código línea por línea:

temp = a: temp guarda una copia del valor de a (es decir, 1).

a = b: a sobrescribe su valor y ahora pasa a valer 2 (el valor de b). Aquí habríamos perdido el 1 original si no lo hubiéramos respaldado antes en temp.

b = temp: b toma el valor guardado en temp (que era 1).

Al final: a queda valiendo 2 y b queda valiendo 1. ¡Logramos intercambiar sus valores!

La variable temp (temporal) sirvió precisamente como una "caja auxiliar" o un respaldo de seguridad para no destruir el valor de a antes de pasárselo a b.
"""
# ---------------------------------------------------------------------

# Condiciones y Toma de Decisiones(if/else)

edad_1 = 18
if edad_1 >= 18:
    mensaje = "Eres mayor de edad"
else:
    mensaje = "Eres menor de edad"

"""
(Nota: elif es la forma en Python de decir "si no se cumplió lo anterior, pero sí se cumple esto...").

Pregunta:
Siguiendo las condiciones en orden de arriba hacia abajo, ¿cuál será el valor final de la variable resultado y por qué?
"""
puntaje = 75

if puntaje > 80:
    resultado = "Aprobado con honores"
elif puntaje >= 60:
    resultado = "Aprobado"
else:
    resultado = "Reprobado"

"""
Mi respuesta: El resultado será "Aprobado", debido que no es mayor de 80 no es aprobrado con honores pero si cumple ser mayor de 60 por lo tanto la condicion se cumple.

Respuesta ideal: Efectivamente, como 75 no es mayor que 80, la primera condición se ignora. Luego, el programa evalúa el elif puntaje >= 60, y como $75 >= 60 , esa condición es verdadera, por lo que guarda "Aprobado" e inmediatamente ignora el resto del bloque (else).
"""

# ---------------------------------------------------------------------

# Operadores Lógicos (and, or, not)

tengo_dinero = True
tengo_tiempo = False

# Con AND: Necesito AMBAS cosas verdaderas para ir de viaje
puedo_viajar = tengo_dinero and tengo_tiempo  # Daría False

# Con OR: Me basta con TENER UNA de las dos para descansar
puedo_descansar = tengo_dinero or tengo_tiempo  # Daría True

esta_lloviendo = False

# Negamos el valor: no está lloviendo -> True
hace_buen_tiempo = not esta_lloviendo  # Da True

"""
Pregunta de lógica:
Imagina que un parque de atracciones tiene la siguiente regla de acceso para una montaña rusa.
¿Cuál es el valor final de la variable puede_subir (True o False) con los datos dados (edad = 14 y estatura = 1.50)?

Si cambiáramos los datos a edad = 10 y estatura = 1.50, ¿cuál sería el valor de puede_subir y por qué?
"""
edad = 14
estatura = 1.50  # en metros

# Regla: Puede subir si tiene al menos 12 años Y mide 1.40 metros o más.
puede_subir = (edad >= 12) and (estatura >= 1.40)

"""
Mi respuesta: Con los datos iniciales, el resultado seria True(verdadero) ya que cumple con las dos condiciones. Pero si cambiamo los datos a edad = 10 y estatura = 1.50, el resultado seria False (falso) ya que no cumple con la primera condicion de tener al menos 12 años y la condicion es que ambas deben cumplirse para que pueda subir, por lo tanto el resultado seria False.
"""

# ---------------------------------------------------------------------

# Ciclos y Bucles (for, while)

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

"""
pregunta de lógica:
Imagina que tenemos una lista de números y queremos contar cuántos números son mayores a 10 usando un bucle
Analizando el recorrido del bucle paso a paso sobre la lista [4, 15, 8, 20, 3]:

¿Cuál será el valor final de la variable contador al terminar de ejecutarse el bucle y por qué?
"""
numeros = [4, 15, 8, 20, 3]
contador = 0

for num in numeros:
    if num > 10:
        contador = contador + 1

"""
Mi respuesta: Al correr el bucle for este compara cada número de la lista y la condicion es que si un número es mayor a 10, el contador incrementara en 1. Los unicos nuneros que cumplen esa función son el 15 y 20 por lo que la variable contador al final del bucle tendra un valor de 2.
"""

# Ciclo while

contador = 1

while contador <= 3:
    print(contador)
    contador = contador + 1  # Incrementamos para no crear un bucle infinito


"""
Rastreando el valor de x en cada vuelta del bucle:

¿Cuántas veces se ejecuta el bloque dentro del while?

¿Cuál es el valor final de x cuando el bucle se detiene?
"""
x = 10

while x > 4:
    x = x - 2

"""
Mi respuesta: El bloque dentro del while se ejecuta 3 veces, ya que en la primera vuelta x pasa de 10 a 8, en la segunda vuelta de 8 a 6 y en la tercera vuelta de 6 a 4. Cuando x es igual a 4, la condición del while (x > 4) ya no se cumple, por lo que el bucle se detiene. Por lo tanto, el valor final de x cuando el bucle se detiene es 4.
"""
# ---------------------------------------------------------------------

# Funciones


def saludar(nombre):
    return f"Hola, {nombre}!"


# Llamamos a la función con el argumento "Leonardo"
mensaje = saludar("Donatello")  # Debera guardar "Hola, Donatello!"

"""
Si llamamos a esta función dos veces de la siguiente manera:

compra1 = calcular_total(100, True)

compra2 = calcular_total(100, False)

¿Cuál será el valor final almacenado en compra1 y cuál en compra2? Explícame brevemente por qué.
"""


def calcular_total(precio, es_estudiante):
    if es_estudiante:
        descuento = precio * 0.10  # 10% de descuento
    else:
        descuento = 0

    precio_final = precio - descuento
    return precio_final


"""
Mi respuesta: El valor final almacenado en compra1 será 90.0, ya que al ser estudiante se aplica un descuento del 10% sobre el precio de 100, resultando en un precio final de 90.0. Por otro lado, el valor final almacenado en compra2 será 100.0, ya que al no ser estudiante no se aplica ningún descuento y el precio final permanece igual al precio original de 100.
"""
# ---------------------------------------------------------------------

# Ámbitos de variables(Local y Global)
x = 5  # Variable GLOBAL


def mi_funcion():
    x = 20  # Variable LOCAL (no cambia la 'x' global)
    print("Dentro:", x)


mi_funcion()
print("Fuera:", x)

"""
Al finalizar la ejecución de esas líneas:

¿Cuál es el valor que queda almacenado en la variable global total?

¿Cuál es el valor almacenado en la variable resultado?

Explícame por qué el valor de la variable total cambia (o no cambia).
"""
total = 100


def agregar_propina(subtotal):
    total = subtotal + 15
    return total


resultado = agregar_propina(50)

'''
Mi respuesta: El valor que queda almacenado en la variable global total es 100, ya que la función agregar_propina crea una nueva variable local total dentro de su propio ámbito y no afecta a la variable global. Por otro lado, el valor almacenado en la variable resultado es 65, ya que se calcula sumando 15 al subtotal de 50 dentro de la función. El valor de la variable total no cambia porque la asignación dentro de la función se realiza en un ámbito local, y no tiene efecto sobre la variable global con el mismo nombre.
'''
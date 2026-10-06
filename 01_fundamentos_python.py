# Variables y Tipos de Datos

#Guardamos un texto (String)
nombre = "Leonardo"

# Guardamos un número entero (Integer)
edad = 16

# Guardamos un número decimal (Float)
estatura = 1.98

#Tu primera pregunta de lógica y deducción:
#Imagina que ejecutamos estas dos líneas de código en Python:

x=10
y=5

x=y

'''
Mi deducción es que teniendo en cuenta que la variable no es constante, el valor se sobreescribe
por lo tanto x toma el valor de y, es decir, x=5. Por lo tanto, si imprimimos x, el resultado será 5.
'''
#---------------------------------------------------------------------
#Intercambio de Valores y Reasignación 
a=1
b=2

#Queremos intercammbiar sus valores usando una variable temporal
temp = a
a = b
b = temp

#siguiente pregunta de lógica:
#Siguiendo paso a paso la ejecución del programa (de arriba hacia abajo):

temp = a
a = b
b = temp


'''
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
'''
#---------------------------------------------------------------------

#Condiciones y Toma de Decisiones(if/else)

edad_1 = 18
if edad_1 >=18:
    mensaje = "Eres mayor de edad"
else:
    mensaje= "Eres menor de edad"

'''
(Nota: elif es la forma en Python de decir "si no se cumplió lo anterior, pero sí se cumple esto...").

Pregunta:
Siguiendo las condiciones en orden de arriba hacia abajo, ¿cuál será el valor final de la variable resultado y por qué?
'''
puntaje = 75

if puntaje > 80:
    resultado = "Aprobado con honores"
elif puntaje >= 60:
    resultado = "Aprobado"
else:
    resultado = "Reprobado"

'''
Mi respuesta: El resultado será "Aprobado", debido que no es mayor de 80 no es aprobrado con honores pero si cumple ser mayor de 60 por lo tanto la condicion se cumple.

Respuesta ideal: Efectivamente, como 75 no es mayor que 80, la primera condición se ignora. Luego, el programa evalúa el elif puntaje >= 60, y como $75 >= 60 , esa condición es verdadera, por lo que guarda "Aprobado" e inmediatamente ignora el resto del bloque (else).
'''

#---------------------------------------------------------------------

#Para fines educativos, se utilizará la librería TextBlob para corregir la gramática de un texto ingresado por el usuario. A continuación, se presenta un ejemplo de cómo implementar esta funcionalidad en Python. creditos a su autor: CLcoding.com
#NO olvides instalar la librería TextBlob si aún no lo has hecho. Puedes hacerlo ejecutando el siguiente comando en tu terminal o línea de comandos:
# pip install textblob
#Corrige solo en ingles por el momento, si deseas corregir en español, puedes explorar otras librerías o servicios de corrección gramatical que soporten el idioma español.
from textblob import TextBlob

def correct_grammar(text):
    blob=TextBlob(text)
    corrected_text= str(blob.correct())
    return corrected_text

text= input("Enter a sentence: ")
corrected_text= correct_grammar(text)

print(f"Corrected sentence: {corrected_text}")

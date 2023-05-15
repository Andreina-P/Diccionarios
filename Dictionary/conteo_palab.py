texto = "Hola soy Andreina de la Escuela Politecnica Nacional !!. Actualmente estoy cursando segundo semestre. Hola"
#Esta variable va aservir para que quede solo el texto, sin ningun signo de puntuacion
signos = ",;.-!:"
for signs in signos:
    texto = texto.replace(signs, "")
#esta variable sirve para convertir el texto en minusculas (tambien podria convertirlo todo en mayusculas
text_in_lower = texto.lower()
text_in_lower = text_in_lower.split()
dictyonary = {}
for palabra in text_in_lower:
    if palabra in dictyonary:
        dictyonary[palabra] +=1
    else:
        dictyonary[palabra]=1

for palabra in dictyonary:
    frecuencia = dictyonary[palabra]

print(dictyonary)
#Se  va a ordenar el diccionario en orden alfabetico
ordered_dictyonary = {}
palabras = dictyonary.keys()
ordered_words = sorted(palabras)

for key in ordered_words:
    ordered_dictyonary [key] = dictyonary[key]

print(ordered_dictyonary)
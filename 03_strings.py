my_string="hola, como estas ?"
my_other_string="bien, bien y tu ?"

#define la longitud de una cadena de texto 
print(len(my_string))
print(len(my_other_string))

#concatenacion de cadenas de texto

print(my_string + " " + my_other_string)

#se pueden definir variables en una sola linea con su respectivo valor
#pero se considera una mala practica 

letras, numeros = "abcde", "67890"

texto= "las letras son: {} y los numeros son: {}".format(letras, numeros)

print(texto)

#para formatear mas comodo existe el print(f'') en este podras especificar las variables directamente
texto_f = f"las letras son: {letras} y los numeros son: {numeros}"
print(texto_f)

#para hacer saltos de linea se utiliza \n
texto_multilinea = "esto es un texto\nque abarca varias"   
print(texto_multilinea)

#para hacer una tabulacion es con \t
texto_tabulado = "item1\titem2\titem3"
print(texto_tabulado)

#Desempaquetado de caracteres
Text_1= "python"

a, b, c, d, e, f = Text_1

print(Text_1)

language= Text_1[0:2] #py
version= Text_1[2:6] #thon
print(language)
print(version)

#al reves 
reversed_text= Text_1[::-1]
print(reversed_text)
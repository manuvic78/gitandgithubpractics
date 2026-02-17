"""tipos de datos en python
str, int, bool, float, list, tuple
"""

a='hola'#tipo de dato string
b= -25#tipo de dato entero
c= True#tipo de dato booleano
d= 25.5#tipo de dato float
e=[1,2,3,4,'hola', 2.5]#lista
f=(1,2,3,4)#tupla
g={'nombre': 'mouredev', 'edad': 35}#diccionario
My_variable_complex= 3 + 5j  #tipo de dato complejo
My_set_variable= {1, 2, 3, 4}  #tipo de dato set


#se puede usar un solo print para ver varios tipos de datos
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(My_variable_complex), type(My_set_variable)) 
print(g['edad'])#acceder al valor de una clave en un diccionario      

""""apuntes claves en todo mi aprendizaje te dejo esto comentarios 

a ti victor del futuro que estas leyendo esto:
- type(): me ayuda a conocer el tipo de dato de una variable
- Los tipos de datos en python son dinamicos, no es necesario declararlos
- Las listas son mutables, las tuplas no lo son
- Los diccionarios almacenan datos en pares clave-valor
- Los sets son colecciones desordenadas de elementos unicos
- Los datos complejos tienen una parte real y una parte imaginaria
- Los comentarios en python se hacen con el simbolo #
- Las cadenas de texto (str) se pueden definir con comillas simples o dobles    
- Los numeros enteros (int) pueden ser positivos o negativos
- Los numeros de punto flotante (float) representan numeros reales con decimales
- Los valores booleanos (bool) pueden ser True o False
- Las listas (list) pueden contener elementos de diferentes tipos de datos
- Las tuplas (tuple) son similares a las listas pero son inmutables
- Las variables en python no requieren una declaracion explicita de su tipo
- Python es un lenguaje de tipado dinamico, lo que significa que el tipo de dato de una variable puede cambiar durante la ejecucion del programa
-Python declara sus variables mediante el snakee_case, es decir, con guiones bajos entre palabras"""
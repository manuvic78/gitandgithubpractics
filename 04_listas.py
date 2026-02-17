"""una lista es un conjunto de datos agrupados bajo una misma variable
las listas se definen con corchetes [] y pueden contener diferentes tipos de datos
ademas las listas son mutables, es decir que se pueden modificar sus elementos"""
my_list = ["hola", 23, 3.14, True]
my_other_list = [1, 2, 3, 4, 5, 1,4,4,4,4,4,4,4]
print(my_other_list.count(4))
#el metodo .count() cuenta la cantidad de veces que un elemento se repite en la lista
#aqui se mide la longitud de la lista con len()
print(len(my_list))
print(len(my_other_list))   

#acceder a los elementos de una lista por su indice
print(my_list[0])  #primer elemento
print(my_other_list[5]) #ultimo elemento

#desempaquetado de listas
a, b, c, d = my_list
print(a)
print(b)    
print(c)
print(d)


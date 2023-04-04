

lista = ["chicago", "queens", 'salvador', 'pernambuco']
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista2 = lista2 + lista3 

lista4 = [True, False]
print(lista4)

# index     0       1       2     3    4  5   -> 6 elementos
lista5 = [True, "chicago", 2.5, False, 4, 8]
print(lista5)

print(type(lista2))

print(lista5[1])

print(lista5[-6])

# Slicing

print(lista5[::])   # dois pontos representa começo e fim
print(lista5[1:])   # retorna do index que destacamos até o fim da lista
print(lista5[2:])   # retorna do index que destacamos até o fim da lista
print(lista5[:3])   # retorna do começo da lista até o index -1
print(lista5[:4])   # retorna do começo da lista até o index -1
print(lista5[1:4])  # retorna do index destacado até o index -1
print(lista5[1:6:2])

nome5 = "terra"

print(nome5[2:4])


lista1 = [2.0, 3.5, 4.7]
print(lista1)

lista2 = [1, 5, 9, 11, 15]
print(lista2)

# index     0         1          2         3         4         5
lista3 = ['gato', 'cachorro', 'peixe', 'cavalo', 'tubarão', 'girafa']

print(len(lista3))

print(type(lista3))
print(lista[1])

lista[1] = 'cavalo'
print(lista)

lista[1:4] = ['águia', 'morcego', 'elefante']
print(lista)

lista[1:2] = ['águia', 'elefante']
print(lista)

# Tamanho da lista - função len
print(len(lista1))
print(len(lista2))

# Funções que só podem ser utilizadas com tipos de dados numéricos

print(sum(lista1))  # Somatório dos elementos da nossa lista
x = 2.0 + 3.5 + 4.7
print(x)

print(max(lista2))  # Retorna o elemento de valor máximo da lista

print(min(lista1))  # Retorna o elemento de valor mínimu da lista


nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list("Curso de Python")
print(lista8)

elemento = 8

if elemento in lista7:
    print("Este elemento está dentro da lista")


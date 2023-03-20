"""
Python - Comandos de controle condicional

if, else e elif -> (else if)



x = float(input("Digite 1 número: "))
y = float(input("Digite 2 número: "))

if y > x:
    print("y é maior do que x")
    print("Código dentro do bloco condicional if")
elif y < x:
    print("y é menor do que x")
elif y == x:
    print("x é igual a y")
else:
    print("y não é menor e nem maior que x")
print('Código fora do bloco condicional')
print(y > x)
print(y < x)
print(y == x)
"""
a = 5
b = 8
c = 2

""" if b > a: print("b é maior que a")
print("Código fora do bloco if") """

"""print("B") if b > a else print("A") # Operador ternário, Expressões Condicionais
"""

if a > b:
    print("A")
    if a > c:
        print("A é maior que b e c")

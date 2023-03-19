"""
Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado
03 - se o produto que você que avaliar custa (??) reais qual
será o valor do mesmo com desconto de (??)%.
04 - aréa de círculo - pi = 3,141592
05 - conversão de reais para dolar
06 - conversão de dolar para reais

"""
# Exercícios 01 - área do retângulo
print("Calcule a área de um retangulo")

base = float(input("Escreva a base do retangulo: "))
altura = float(input("Escreva a altura do retangulo: "))
area = base * altura

print(f"O seu retangulo possui a área: {area} unidade de medida")

# Exercícios 02 - área de um quadrado
print("Calcule a área de um quadrado")

b = float(input("Escreva a base do quadrado: "))
h = float(input("Escreva a altura do quadrado: "))
a = b * h

print(f"O seu quadrado tem a área de {a}")

# Exercícios 03 - se o produto que você que avaliar custa (??) reais qual será o valor do mesmo com desconto de (??)%.
p = int(input('Qual é o preço do produto? '))
d = int(input('Qual é o desconto do produto? '))

pd = p - (d / 100) * p

print(f'O preço do produto é R${p:.2f} O desconto é {d:.2f}% O produto com desconto fica R${pd:.2f}')

# Exercícios 04 - aréa de círculo - pi = 3,141592
raio = float(input('Qual o raio do seu circulo? '))
pi = 3.141592
area = pi * raio**2

print(f'A área do círculo é: {area:.2f}')
# Exercícios 05 - conversão de reais para dolar
cotacao = 5.50
reais = float(input('Quanto reais você quer converter em dolar? '))

dolar = reais / cotacao

print(f'R$ {reais:.2f} equivalem a US${dolar:.2f}')

# Exercícios 06 - conversão de dolar para reais
cotacao = 5.50
dolar = float(input('Quanto dolar você quer converter em reais? '))

reais = dolar * cotacao

print(f'US${dolar:.2f} equivalem a R${reais:.2f}')

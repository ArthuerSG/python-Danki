"""
Descobrir se um número é primo

"""

print(30 * "-")

numero = int(input("Insira um número para descobrir se o mesmo é primo: "))

if numero > 1:
    for x in range(2, numero):
        if (numero % x) == 0:
            print("Esse não é um número primo")
            break
    else:
        print("Esse é um número primo")
else:
    print('Esse número não é primo: número menor ou igual a 1')
print(30 * "-")

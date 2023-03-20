# 01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de acordo com os critérios:
# ● Menor de 16 anos: MENOR
# ● Entre 16 e 18 anos: EMANCIPADO
# ● Maior de 18 anos: MAIOR
idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("MENOR")
elif idade >= 16 and idade < 18:
    print("EMANCIPADO")
else:
    print("MAIOR")

# 02 - Implemente um programa que receba a idade de um nadador e imprima a sua categoria seguindo as regras:
#
# CATEGORIA     IDADE
# Infantil A    5-7 anos
# Infantil B    8-10 anos
# Juvenil A    11-13 anos
# Juvenil B    14-17 anos

idade = int(input("Digite a sua idade: "))

if idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 10:
    print("Infantil B")
elif idade >= 11 and idade <= 13:
    print("Juvenil A")
else:
    print("Juvenil B")

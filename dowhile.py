"""
do while

Código para adivinha um número

"""

palpite = 5
numero = 9

while bool(palpite) is True:    # Nós executamos sem verificar
    print("Qual o número correto? ")
    palpite = int(input())
    if palpite == numero:   # Estamos verificando nosso código
        print("Parabens você acertou")
        break
    else:
        print("Você errou")
else:
    print(bool(palpite))

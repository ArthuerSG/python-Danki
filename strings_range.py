#   0123456
nome = "chigago"

print(nome[1])
 
for x in range(10, 0, -1):
    print(x)

nome = "chigago"
nome2 = "queens"

print(nome, end=" ")
print(nome2)

nome = "chigago"

for x in nome:
    print(x, end="#")

x = 5
y = 0

x, y = y, x

print(x)
print(y)

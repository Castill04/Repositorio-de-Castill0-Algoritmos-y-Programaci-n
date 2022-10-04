n = int(input("Inserte un numero: "))
np = 0
ni = 0
p = True

while p:
    for i in range(1, n + 1):
        if i % 2 == 0:
            np += 1
        elif i % 2 != 0:
            ni += 1
    p = False

print(f"Los numeros pares son: "(np))
print(f"Los numeros impares son: "(ni))


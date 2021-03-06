l1 = []
l2 = []
for i in range(6):
    valorL1 = int(input("Digite um número para a lista l1: "))
    valorL2 = int(input("Digite um número para a lista l2: "))
    l1.append(valorL1)
    l2.append(valorL2)

l3 = l1 + l2
# coloca em ordem crescente
l3 = sorted(l3)
# interte a lista  l3 é coloca em l4
l4 = sorted(l3, reverse=True)
l5 = []
# pecorreu a lista 1
for c in range(len(l1)):
    # elementos em comum entre l1 e l2
    # se os elementos de lista 1 esta em lista 2
    if(l1[c] in l2):
        # para não colocar elementos iguais da mesma lista
        if(l1[c] not in l5):
            l5.append(l1[c])
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

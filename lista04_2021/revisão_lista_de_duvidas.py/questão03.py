lista1 = []
lista2 = []

for i in range(6): #12
    n = int(input(f'Digite os números {i+1} para lista 1  :'))
    n2 = int(input(f'Digite os números {i+1} para lista 2 '))
    lista1.append(n)
    lista2.append(n2)

# concatene junta as duas listas 
l3 = sorted(lista1+lista2)
l4 = l3
l4 = sorted(l3, reverse=True)
l5 = []
# pecorreu a lista 1 entrege na variável elementos 
for elementos in range(len(lista1)):
    # elementos em comum entre l1 e l2
    # se os elementos de lista 1 esta em lista 2
    if lista1[elementos] in lista2:
        # para não colocar elementos iguais da mesma lista
        if lista1 not in l5:
            l5.append(lista1[elementos])
print(lista1)
print(lista2)
print(l3)
print(l4)
print(l5)

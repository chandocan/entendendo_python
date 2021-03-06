'''
Escreva um programa para pedir ao usuário duas listas de 10 componentes
inteiros cada e determinar o conjunto união para os conjuntos lidos.
Imprima a lista contendo conjunto união, ao final. Não permita adição de
números repetidos em uma mesma lista. O conjunto união não pode ter
números repetidos.

'''
lista1 = []
lista2 = []
uniao = []
for x in range(6): # 10
    e = int(input(f'digite o componente {x+1} :'))
    if e not in lista1:
        lista1.append(e)
for i in range(6):
    c = int(input(f'digite os componentes {i+1} :'))
    if c not in lista2:
        lista2.append(c)
for elemento in lista1:
    if elemento not in uniao:
        uniao.append(elemento)
for elemento in lista2:
    if elemento not in uniao:
        uniao.append(elemento)
print(lista1)
print(lista2)

print(f'o conjunto união é = {sorted(uniao)}')

# outra foram 
a = lista1
b = lista2

print(a)
print(b)
# elemento = i
for i in a:
    # elemento = b
    for j in b:
        if (i == j):
            b.remove(j)

print(a) # lista 'a' normal sem alteração
print(b) # lista 'b' menos os elementos iguais das duas litas

uniao = a + b
print(sorted(uniao))

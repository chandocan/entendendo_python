a = [ 'a', 'i' , 'u', 'o']
b = ['a', 'e', 'o' , 'z']

print(a)
print(b)

for i in a:
    for j in b:
        if (i == j):
            b.remove(j)

print(a) # lista 'a' normal sem alteração
print(b) # lista 'b' menos os elementos iguais das duas litas

uniao = a + b
print(uniao)
# outra forma de fazer
a = [ 'a', 'i' , 'u', 'o']
b = ['a', 'e', 'o' , 'z']

print(a)
print(b)

uniao = []

for letra in a:
    if (letra not in uniao):
        uniao.append(letra)

for letra in b:
    if (letra not in uniao):
        uniao.append(letra)

print(uniao)
a= [ 'a', 'i' , 'u', 'o']
b = ['a', 'e', 'o' , 'z']

print(a)
print(b)

uniao = []

for letra in a:
    # se letra não esta em uniao ela vai add se esta não vai adicionar (esta dentro do conjunto não entra nada)
    if (letra not in uniao):
        uniao.append(letra)

for letra in b:
    if (letra not in uniao):
        uniao.append(letra)

print(uniao)

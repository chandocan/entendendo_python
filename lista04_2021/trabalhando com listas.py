# cria uma lista c0om a quantidade determinada no range 
lista = list(range(5))
print(lista)
# do tipo inteira
print(type(lista[1]))
print(type(lista))
lista2 = ['ana', 'karla','sabrina']
# da para junta duas listas
r = lista + lista2
print(r)
# da para encachar esse elementos em qualquer lugar num print
print(f'{r[7]} receneu elemento {r[3]}')
# print do ultimo valor
print(r[-1])
# para usa isso aqui tem que esta escrito da mesma forma é se tiver espaço tambem 
# tem que ter os espaço contam como nome na string , mesmo que in(esta) 
print('sabrina' in r)
# estou lendo os intens de uma lista
# como se tivesse pecorrendo a lista para saber os itens interando interação com r é x
for x in r:
    print(x)
# tamanho da lista
print('A lista tem po tamaho de ',len(r), 'elementos')
for i in r:
    print(i)
    print( )
print('total de elementos ',len(r))
# usei um range para interação de uma lista h com a variavel i para pecorre com range
h = ['ana', 'jose', 'dayse']
for i in range(3):
    print(h[i])
# se sabemos o tamanho da para fazer uma soma nos elementos
k = [1,2,3,10,20]
for i in range(len(k)):
    # somando todos os elementos com + 1
    k[i] += 1
    print(k[i])
# soma todos os elementos da lista colocada na variava_soma abaixo
variavel_soma = 0
for i in range(len(k)):
    #variavel_soma = variavel_soma + k[i]
    variavel_soma += k[i]
# somou todos os elementos da lista
print('soma total = ',variavel_soma)

# para remover os itens da lista é não guarda
t = ['a' , 'b', 'c']
print(t)
print('retirou o b')
del t[1]
print(t)
# para apagar mais de um item da lista 
del t[1:2]
print('removel b é o elemento c ficando só o elemento a')
print(t)
# usando pop
# se não colocar nada no parentece do pop ele apaga o ultimo elemento
# ele pode guadar o que apagou
b = ['a','b','c']
x = b.pop(1)
print('A lista ficou assim no final')
print(b)
print('exibiu o elemento removido aqui ',x)

# pode remover por valor 

queijo = ['coalho','ricota','gorgonzola']
queijo.remove('coalho')
print(queijo)

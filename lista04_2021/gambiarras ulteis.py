# gambiarras em python

lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
uniao =  []
# Obs para pecorre os dois for dessa forma temos que ter os dois for anteriores iguais em seu range
# PECORREU AS DUAS LISTA COM UM FOR ASSIM
for i in range(len(lista1) and (len(lista2))):
#for i in range(6): # da para simplificar assim se os for da cunstrução das listas anteriores forem iguais 
        uniao.append(lista1[i])
        uniao.append(lista2[i])
print('a lista de chamada foi ',uniao)

# outra forma de não colocar elementos repetitivos em uma lista
from itertools import chain

a = [1, 2, 3]
b = [3, 4, 5]

c = list()
for item in chain(a, b):
    if item not in c:
        c.append(item)

c.sort()
print(f'\033[32mA lista resultante é: {c}')

# esse de união é interceção
lista1 = []
lista2 = []
uniao = []
intercao = []
for i in range(6): # 10
    elemento = int(input(f'diga o elementos {i+1} da lista 1 :'))
    elemento2 = int(input(f'diga o elementos {i+1} da lista 2:'))
    if elemento != elemento2:
        lista1.append(elemento)
        lista2.append(elemento2)
    if elemento != elemento2:
        uniao.append(elemento)
        uniao.append(elemento2)
    if elemento == elemento2:
        intercao.append(elemento)    
print(lista1)
print(lista2)            
print('conjunto união é ',uniao)
print('interceao',intercao)

# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
# de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
nota_lida = 0
notas_lidas = []

while nota_lida != -1:
    nota_lida = float(input("Digite a nota ou -1 para encerrar: "))
    if nota_lida != -1:
        notas_lidas.append(nota_lida)
        
# Mostre a quantidade de valores que foram lidos;
print("A. Quantidade de valores que foram lidos:", len(notas_lidas))

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print("B. Valores na ordem em que foram informados, um ao lado do outro:", notas_lidas)
for nota in notas_lidas:
    print(nota, end=" ")
    
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("\nC. Valores na ordem inversa à que foram informados, um abaixo do outro:")
for indice in range(len(notas_lidas)-1, -1, -1):
    print(notas_lidas[indice])
    
# Calcule e mostre a soma dos valores
print("D. Soma dos valores")
print("\tUsandao a função Sum:", sum(notas_lidas))
print("\tUsando for e somando 1 a 1: ", end="")
soma = 0
for nota in notas_lidas:
    soma += nota
print(soma)

# Calcule e mostre a média dos valores
media = soma/len(notas_lidas)
print("E. A média das notas:", media)

# Calcule e mostre a quantidade de valores acima da média calculada;
print("F. Quantidade de valores acima da média: ", end="")
acima_media = 0
for nota in notas_lidas:
    if nota > media:
        acima_media += 1
print(acima_media)

# Calcule e mostre a quantidade de valores abaixo de sete;
print("G. Quantidade de valores abaixo de sete: ", end="")
abaixo_7 = 0
for nota in notas_lidas:
    if nota < 7:
        abaixo_7 += 1
print(abaixo_7)

# Encerre o programa com uma mensagem;
print("Programa encerrado.")

# ADICIONANDO ELEMENTOS SEM REPETILOS EM OUTRA LISTA
'''
Escreva um programa para pedir ao usuário duas listas de 10 componentes
inteiros cada e determinar o conjunto união para os conjuntos lidos.
Imprima a lista contendo conjunto união, ao final. Não permita adição de
números repetidos em uma mesma lista. O conjunto união não pode ter
números repetidos.

'''
# só funciona com números
from itertools import chain
lista1 = []
lista2 = []
intercecao = []
for i in range(6): # 10
    elemento = int(input(f'diga o elementos {i+1} da lista 1 :'))
    elemento2 = int(input(f'diga o elementos {i+1} da lista 2:'))
    lista1.append(elemento)
    lista2.append(elemento2)
    if elemento == elemento2:
        intercecao.append(elemento)
uniao = list()
for item in chain(lista1, lista2):
    if item not in uniao:
        uniao.append(item)  
print(lista1)
print(lista2)            
print('conjunto união é ', uniao)
print('interceao',intercecao)
uniao.sort()
print(f'\033[32mA lista resultante é em ordem: {uniao}')

# maneira simples de fazer o exercicio assima
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

#outra forma de fazer
a= [ 'a', 'i' , 'u', 'o']
b = ['a', 'e', 'o' , 'z']

print(a)
print(b)

uniao = []
# pecorre 'a' se letra não esta em união vai add com isso evitar repetição de elemento em união
for letra in a:
    if (letra not in uniao):
        uniao.append(letra)
# pecorre 'b' se letra não esta e união vai add  com isso evita repetição de elemento em união
for letra in b:
    if (letra not in uniao):
        uniao.append(letra)

print(uniao)
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

'''

'''

# para mudar clientes de uma fila para outra
# obs o tamanho do range tem que esta de acordo com o tamanho das fila filas se não vai da erro de fila vazia (empty list)

import time
fila1 = []
fila2 = []
fila3 = []
for i in range(15):
    nome = input('nome do cliente:')
    fila1.append(nome)
    if len(fila1) == 5:
        fila2.append(fila1.pop(0))
    if len(fila2) == 5:
        fila3.append(fila2.pop(0))
    print('fila 1',fila1)
    print('fila 2',fila2)
    print('fila 3',fila3)
for i in range(15):
    fila3.pop(0)
    if len(fila1) > 0 :
        fila2.append(fila1.pop(0))
    if len(fila2) > 0 :
        fila3.append(fila2.pop(0))
    print(fila1)
    print(fila2)
    print(fila3)
    time.sleep(3)
'''
Um restaurante possui um sistema de atendimento que funciona da seguinte forma: O cliente passa pelas
 seguintes filas:
1° fila: o cliente faz seu pedido, saindo desta fila ele entra em uma segunda fila; 
2° fila: o cliente realiza o pagamento do seu pedido, saindo desta segunda fila ele entra em uma terceira fila;
3° fila: entrega do pedido do cliente.
Cada um das 3 filas tem espaço pra 5 pessoas. O programa pedirá 15 clientes, assim 
que a primeira fila estiver cheia, o cliente será removido da fila de pedidos e irá para a fila de pagamento. 
Isso se repete e quando a fila de pagamento estiver cheia, o cliente deverá ser removido para ir para a fila de entrega
de pedido. A cada movimentação as 3 filas deverão ser impressas. O programa termina quando o último cliente tiver seu
pedido entregue, ou seja, as filas estiverem vazias
'''
import time
fila1 = []
fila2 = []
fila3 = []
for i in range(15):
    nome = input(f'nome do cliente {i+1} :')
    fila1.append(nome)
    if len(fila1) == 5: # tamanho das filas
        fila2.append(fila1.pop(0))
    if len(fila2) == 5:
        fila3.append(fila2.pop(0))
    if len(fila3) == 5:
        fila3.pop(0)
    # fila com os 5 clientes aqui
    print('fila 1',fila1)
    print('fila 2',fila2)
    print('fila 3',fila3)
    # responsavel por esvaziar as filas 
for x in range(15):
    if len(fila1) > 0:
        fila2.append(fila1.pop(0))
    if len(fila2) > 0:
        fila3.append(fila2.pop(0))
    if len(fila3) > 0:
        fila3.pop(0)
  
    print('esvaziando 1',fila1)
    print('esvaziando 2',fila2)
    print('esvaziando 3',fila3)
    if len(fila3) == 0:
        break
    time.sleep(3)


# para pecorre uma lista ou pilha é remove da mesma
pilha45 = ['m','v','c','y','r']
for i in pilha45:
    if nome == i:
        pilha45.remove(nome)
# pecorrendo é imprimindo 
pilha = ['m','v','c','y','r']
for i in pilha:
    print(i, end= ' '), print('elemntos')
    
#invertendo uma lista
v = ['a','c','w','e','z']
x = v[::-1]
print(x)# vai print a lista invertida






## para pecorre lista é compra com numeros

minha_lista = [1,2,3,4,5]
maior_que = 2

filtrados = [x for x in minha_lista if x > maior_que]

#exibe os elementos
print(filtrados)

#conta os elementos
print(len(filtrados))


# outras coisa 
lista = [1,2,3,4,5,6,7,8,9,1,23]
X = 0
B = 0 # Armazena a quantidade de números maiores que 2
num_elementos_lista = len(lista)
while(X < num_elementos_lista):
    if lista[X] > 2: # verifica se lista[X] é maior que 2
      B+=1 # Se for incrementa + 1 em B
    X+=1

print(B+1)






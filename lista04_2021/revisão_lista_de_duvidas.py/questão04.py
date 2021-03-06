'''
4. Crie um programa em Python que tenha uma pilha composta por 10 nomes de pessoas e
permita:
a) Insira novos elementos;
b) Remova elementos;
c) Imprimir o tamanho da pilha;
d) Imprimir o topo da pilha, sem excluir elementos;
e) Imprimir o sub-topo da pilha, sem excluir elementos;
f) Imprimir a base da pilha, sem excluir elementos;
g) Imprimir todos os elementos da pilha sem excluir elementos;
h) Desempilhar N elementos da pilha (OBS: N <= tamanhoDaLista)
i) Esvaziar a pilha.

'''
pilha = ["Gustavo", "Rafael", "Mariana", "Lucas", "Higor", "Juliana",
"Viviane", "Sávio", "Gabriel", "Paula"]

# insera novos elementos (a)
pilha.append('Alfredo')
pilha.append('Marcella')
print('pilha com novo elementos')
print(pilha)
# remova elementos (b)
print('pilha removendo um elemento')
pilha.pop()
print(pilha)
# imprimindo o tamanho da pilha (c)
print('Tamanho da pilha')
print(len(pilha))
# imprimar o top da pilha (d)
print('O topo da pilha')
print(pilha[-1])
# imprimar o sub-topo (e)
print('imprimir o sub-top')
print(pilha[-2])
# imprimar a base (f)
print('A base é')
print(pilha[0])
print('='*70)
# imprimir todos os elementos (g)
print('todos os elementos')
for n  in pilha:
    w1=pilha[10] 
    w2=pilha[9] 
    w3=pilha[8]
    w4=pilha[7]
    w5=pilha[6] 
    w6=pilha[5] 
    w7=pilha[4] 
    w8=pilha[3] 
    w9=pilha[2] 
    w10=pilha[1] 
    w11=pilha[0]
print(w1)
print(w2)
print(w3)
print(w4)
print(w5)
print(w6)
print(w7)
print(w8)
print(w9)
print(w10)
print(w11)

# letra (h)
# Desempilha N elementos da pilha (OBS <= tamanhoDaLista)
# vai desempilhar uma quantidade 'x' de elementos
n = int(input("Digite a quantidade de elementos:"))
# se n for menor ou igual ao tamanho da pilha 
if(n <= len(pilha)):
    # vai da um espaçamento  de 'n'(tantos numeros digitados) em pilha
    for i in range(n):
        # vai remover com forme o numero digitado para o range
        pilha.pop()
    else:
        print("N maior que a quantidade de elementos!")
print(pilha)
#letra (i)
# esvaziar a pilha
# vai deletar toda a pilha do zero indiante
del pilha[0:]
print(pilha)
'''
outra forma de esvaziar
# outra forma de se excluir todos os elementos
# vai excluir todos os elementos ate atingir o tamanho da pilha
for i in range(len(pilha)):
    pilha.pop()
print(pilha)
'''

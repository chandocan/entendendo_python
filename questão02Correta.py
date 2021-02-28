'''
(3,0) Em um estacionamento, que só tem uma entrada, os carros são
estacionados um após ao outro e na hora de retirar um carro, todos os
que estão atrás dele precisam ser retirados. Após a retirada do carro,
todos os demais precisam ser recolocados na ordem que estavam.
Implemente um programa que receba 30 carros (a entrada recebe o nome
dos donos dos carros) e armazena em uma pilha. Após receber os 30
nomes, o programa irá receber o nome do dono que quer retirar o carro.
Precisa checar se o nome do dono consta na pilha (imprima mensagem
de que não existe esse dono, caso contrário), precisa desempilhar os
carros até o carro desejado (use uma segunda pilha), precisa empilhar
novamente o restante. Imprimir a pilha após a remoção. Fazer isso até
que a o usuário digite vazio ou não tenha mais carro. 
'''
pilhaNomes = []
pilhaAux = []
dono = 0 #posição do elemento na pilha.

for i in range(1, 7):

    nome = str(input('Nome do dono: ')).upper()
    pilhaNomes.append(nome)

print()
print('Pilha de Nomes inicial: ',pilhaNomes)
print()

buscarDono = str(input('Nome do dono que deseja remover o carro: ')).upper()

while(buscarDono != ""):

   for i in range(len(pilhaNomes)):

       if(buscarDono == pilhaNomes[i]):
           
           dono = i
           break
     
   for i in range(len(pilhaNomes)):

       if(buscarDono == pilhaNomes[0]): #Caso seja o 1º elemento.

           pilhaNomes.pop(0)
           print('Pilha após a remoção (PRIMEIRO ELEMENTO): ',pilhaNomes)
           break

       if(buscarDono == pilhaNomes[len(pilhaNomes) - 1]): #Caso seja o ultimo elemento.

           pilhaNomes.pop(len(pilhaNomes) - 1)
           print('Pilha após a remoção (ULTIMO ELEMENTO): ',pilhaNomes)
           break

       if(i != dono):

           pilhaAux.append(pilhaNomes.pop())

       if(i == dono):

           pilhaNomes.pop(i)
           break

   if(len(pilhaAux) != 0):
      
       for i in range(len(pilhaAux)):
          
           pilhaNomes.append(pilhaAux.pop())

       print('Pilha após empilhar os elementos novamente: ',pilhaNomes)


   buscarDono = str(input('Nome do dono que deseja remover o carro: ')).upper()

'''
1. (2,0) Um restaurante possui um sistema de atendimento que funciona da
seguinte forma: O cliente passa pelas seguintes filas:
1° fila: o cliente faz seu pedido, saindo desta fila ele entra em uma segunda
fila;
2° fila: o cliente realiza o pagamento do seu pedido, saindo desta segunda
fila ele entra em uma terceira fila;
3° fila: entrega do pedido do cliente.
Cada um das 3 filas tem espaço pra 5 pessoas. O programa pedirá 15
clientes, assim que a primeira fila estiver cheia, o cliente será removido da
fila de pedidos e irá para a fila de pagamento. Isso se repete e quando a fila
de pagamento estiver cheia, o cliente deverá ser removido para ir para a fila
de entrega de pedido. A cada movimentação as 3 filas deverão ser
impressas. O programa termina quando o último cliente ter ser pedido
entregue, ou seja, as filas estiverem vazias.

'''
import time
fila1 = []
fila2 = []
fila3 = []
# total de clientes
for i in range(15):
    cliente = input('DIGITE O NOME DO CLIENTE:')
    # cada fila tem espaço para 5 pessoas por isso o "len(fila) == 5"
    fila1.append(cliente)
    # depois ser removido é entra nas outras filas
    if(len(fila1) == 5):
        fila2.append(fila1.pop(0)) # vai adicionar o primeiro da fila1 = "fila1.pop(0)" na fila2
    if(len(fila2) == 5):
        fila3.append(fila2.pop(0)) # vai adionar o primeiro da fila2 = "fila2.pop(0)" na fila3
    # as filas foram prindadas dentro de um loop do for de lá de cima
    print(fila1)
    print(fila2)
    print(fila3)
# len() é mesmo que tamnaho da lista
for i in range(15):
    time.sleep(2)
    fila3.pop(0) # foi removido 15 fezes tudo que esta na fila3  devido ao loop do for
    if(len(fila1) > 0): # vai remover ate cheaga a zero
        fila2.append(fila1.pop(0))
    if(len(fila2) > 0): # vai remover ate chegar a zero
        fila3.append(fila2.pop(0))
  
    print()
    print(fila1)
    print(fila2)
    print(fila3)

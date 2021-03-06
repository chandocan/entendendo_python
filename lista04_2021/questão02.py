'''
Um restaurante possui um sistema de atendimento que funciona da
seguinte forma: O cliente passa pelas seguintes filas:
1° fila: o cliente faz seu pedido, saindo desta fila ele entra em uma segunda
fila;
2° fila: o cliente realiza o pagamento do seu pedido, saindo desta segunda
fila ele entra em uma terceira fila;
3° fila: entrega do pedido do cliente.
Cada um das 3 filas tem espaço pra 5 pessoas. O programa pedirá 15
clientes, assim que a primeira fila estiver cheia, o cliente será removido da
fila de pedidos e irá para a fila de pagamento. Isso se repete e quando a
fila de pagamento estiver cheia, o cliente deverá ser removido para ir para
a fila de entrega de pedido. A cada movimentação as 3 filas deverão ser
impressas. O programa termina quando o último cliente tiver seu pedido
entregue, ou seja, as filas estiverem vazias. 

'''
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
    if len(fila3) == 5:
        fila3.pop(0)
    print('fila 1',fila1)
    print('fila 2',fila2)
    print('fila 3',fila3)
for i in range(15):

    #fila3.pop(0)
    if len(fila1) > 0 :
        fila2.append(fila1.pop(0))
    if len(fila2) > 0 :
        fila3.append(fila2.pop(0))
    if len(fila3) > 0 :
        fila3.pop(0)
    print(fila1)
    print(fila2)
    print(fila3)
    time.sleep(3)

'''
Uma farmácia atende seus clientes por ordem de chegada. Ela tem uma
fila para clientes normais e um para os clientes prioritários. Crie um
programa que receba 20 clientes e os registre como prioritário ou não. Após
esse cadastro, liste a sequência de clientes, sempre puxando um cliente
normal e um prioritário. (lide de forma correta com as filas vazias)
'''
total_de_clientes = []
list_normal = []
list_prioritario = []

for i in range(20): # 20
    tipo = input('tipo do cliente n ou p:')
    nome = input('nome do cliente :')
    # registros do clientes
    if tipo == 'n':
        list_normal.append(nome)
    if tipo == 'p':
        list_prioritario.append(nome)
# para add os clientes de forma alternada
# para clientes em espaço 20
# liste a sequência de clientes, sempre puxando um cliente 
# normal e um prioritário
for clientes in range(20):
    # precisou ler o tamanho da fila para pode colocar na lista total
    # pois daria um erro de lista inexistente
    # o tanho da lista diferente de zero
    # vai puxa sempre o primeiro de cada lista anterior
    if len(list_normal) != 0:
        # add em  total o primeiro de normal
        total_de_clientes.append(list_normal.pop(0))
    if len(list_prioritario) != 0:
        # add em total o primeiro de prioritario
        total_de_clientes.append(list_prioritario.pop(0))
# todos clientes de forma altendida entre 'normal' e 'prioritario'  
print(total_de_clientes)

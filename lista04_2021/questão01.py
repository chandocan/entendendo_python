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

    if tipo == 'n':
        list_normal.append(nome)
    if tipo == 'p':
        list_prioritario.append(nome)
for clientes in range(20):
    if len(list_normal) != 0:
        total_de_clientes.append(list_normal.pop(0))
    if len(list_prioritario) != 0:
        total_de_clientes.append(list_prioritario.pop(0))
    
print(total_de_clientes)

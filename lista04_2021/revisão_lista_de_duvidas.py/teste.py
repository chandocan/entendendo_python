fila = []
atendidos = []
nome = 0
f = 0
while nome != 5 :
    print('          MENU          ')
    print('(1) Incluir paciente')
    print('(2) Realizar chamada de paciente')
    print('(3) Consultar a posição atual de paciente pelo nome')    
    print('(4) Listar a quantidade de pacientes já atendidos')
    print('(5) Sair')
    # adicionado paciente
    opcao = int(input('digite a opção:'))
    if opcao == 1:
        nome = input('nome do paciente ?:').lower()
        fila.append(nome)
        # quando o paciente chegar é a ordem de chegada
        print("Sua ordem: " , len(fila))
    if opcao == 2:
    # fazer chamada
        chamada = fila.pop(0)
        atendidos.append(chamada)
        print(f'paciente atendido = {atendidos}')
    # consultar
    if opcao == 3:
         # uso da função index mais uma concatenação é outra forma de fazer consumindo menos recurso do pc
        #nome2=input("Insira o nome: ")
        #print('você esta na posição: '+fila.index(nome2)+1)
        for i,n in enumerate(fila):
            nome=input("Insira o nome: ")
            if(nome == n):
                print(f'posição {i+1} nome {n}')
    # paciente atendido
    if opcao == 4:
        print(f'PACIENTES ATENDIDOS = {len(atendidos)}')
    # fim do programa
    if opcao == 5:
        print('programa encerrado')
    else:
        print('digite uma opção do menu')

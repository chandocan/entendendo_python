fila = []
atendidos = []
opcao = 0
while opcao != 5 :
    print("Clínica Médica \n ====================")
    print("(1) Incluir paciente\n(2) Realizar chamada de paciente\n(3) Consultar a posição atual do paciente pelo nome\n(4) Listar a quantidade de pacientes já atendidos\n(5) Sair")
    # mostra os 4 ultimos pacientes
    if len(fila) < 5:
        print('fila atual',fila)
    # adicionado paciente
    opcao = int(input('digite a opção:'))
    if opcao == 1:
        nome = input('nome do paciente ?:').lower()
        fila.append(nome)
        # quando o paciente chegar é a ordem de chegada
        print("Sua ordem: " , len(fila))
    # fazer chamada
    if opcao == 2:
        # aqui poderia ser só um print(fila.pop(0))
        chamada = fila.pop(0)
        atendidos.append(chamada)
        print('Atendimento atual :',chamada)
        
    # consultar vai fazer uma busca consultando o nome
    if opcao == 3:
        # uso da função index é outra forma de fazer consumindo menos recurso do pc
        # somo mais um no index pois o index tem por padrão inicia do zero é sabemos que em fila não existe posição
        # zero por isso do (nome)+1
        # comando com index abaixo
        ##nome2=input("Insira o nome: ")
        ##print('você esta na posição: ',fila.index(nome)+1)
        nome= input('Insira o nome: ')
        for i,n in enumerate(fila):
            if(nome == n):
                print('O paciente é o(a) ',i+1)
                #print(f'posição do paciente é {i+1} , nome {n}')
    # paciente atendido
    if opcao == 4:
        print(f'PACIENTES ATENDIDOS = {len(atendidos)}')
        print(f'paciente atendidos = {atendidos}')
    # fim do programa
    if opcao == 5:
        print('programa encerrado')
    else:
        print('digite uma opção do menu')

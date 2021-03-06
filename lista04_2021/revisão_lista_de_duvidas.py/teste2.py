# tempo da questão 2h : 00
fila=[]
c=0
opcao=0
while(opcao != 5):
    print('          MENU          ')
    print('(1) Incluir paciente')
    print('(2) Realizar chamada de paciente')
    print('(3) Consultar a posição atual de paciente pelo nome')
    print('(4) Listar a quantidade de pacientes já atendidos')
    print('(5) Sair')
    opcao=int(input("Escolha uma opção: "))
    if(opcao==1):
        nome = input("Nome do paciente: ")
        fila.append(nome)
        # ordem vai ser o tamanho da fila
        print("Sua ordem: " , len(fila))
    elif(opcao==2):
        print(fila.pop(0))
        c+=1
    elif(opcao==3):
        nome=input("Insira o nome: ")
        # uso da função index mais uma concatenação
        print('você esta na posição: '+fila.index(nome)+1)
        #for i,n in enumerate(fila):
        #    if(nome == n):
        #        print(i+1)
    elif(opcao==4):
        print(c)
    elif(opcao==5):
        print("Saindo...")
    else:
        print("Digite um número do menu!") 

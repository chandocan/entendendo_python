'''
5. Uma clínica médica utiliza um sistema para controlar a ordem de atendimento de seus 
pacientes que possui o seguinte menu:
Clínica Médica
=============
(1) Incluir paciente
(2) Realizar chamada de paciente
(3) Consultar a posição atual de paciente pelo nome
(4) Listar a quantidade de pacientes já atendidos
(5) Sair
O critério de atendimento é a ordem de chegada. O paciente deve fornecer seu nome. 
Após isso o paciente é adicionado ao sistema e deve aguardar sua vez. Assim que um paciente 
for adicionado o sistema deverá fornecer a sua ordem de atendimento
'''
fila=[]
c=0
print("Clínica Médica \n ====================")
print("(1) Incluir paciente\n(2) Realizar chamada de paciente\n(3) Consultar a posição atual do paciente pelo nome\n(4) Listar a quantidade de pacientes já atendidos\n(5) Sair")
opcao=0
while(opcao != 5):
    opcao=int(input("Escolha uma opção: "))
    if(opcao==1):
        nome = input("Nome do paciente: ")
        fila.append(nome)
        # quando o paciente chegar é a ordem de chegada
        print("Sua ordem: " , len(fila))
    elif(opcao==2):
        # vai imprimir o primeiro da fila que é o primeiro a ser chamado
        print(fila.pop(0))
        # contando todos os pacientes atendidos
        c+=1
    elif(opcao==3):
        # vai fazer uma busca consultando o nome
        nome=input("Insira o nome: ")
        #print(fila.index(nome)+1)
        for i,n in enumerate(fila):
            if(nome == n):
                print(i+1)
    elif(opcao==4):
        # só fez printa a quantidade de pacientes atendidos com o contador
        print(c)
    elif(opcao==5):
        # um print só para ilustra
        print("Saindo...")
    else:
        print("Digite um número do menu!") 

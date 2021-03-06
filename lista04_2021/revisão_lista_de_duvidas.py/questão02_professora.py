totalGeral = 0
for x in range(2):
    totalC = 0
    contItens = "Sim"

    nome = input("Digite o nome do cliente: ")
    while contItens != "Não" :
        item = int(input("Digite a opção desejada: "))
        quantidade = int(input("Digite a quantidade: "))

        if(item == 1):
            totalC += 5.1 * quantidade
        elif(item == 2):
            totalC += 8 * quantidade
        elif(item == 3):
            totalC += 2.55 * quantidade
        else:
            print("opção inválida")

        contItens = input("Quer adicionar mais itens? sim ou não: ")

    print("Total a ser pago %.2f" %totalC)
    totalGeral += totalC
    # continuar pedindo
    contCli = input("Mais clientes para atender? ")
    if contCli == "Não":
        break
print("Total arrecadado no dia %.2f" %totalGeral)

'''
1. Faça um programa que receba o preço de custo e o preço de venda de vários produtos. Para
cada produto informe se houve prejuízo (preço de custo > preço de venda). Ao final da leitura
dos dados informe a média de preço de custo e a média do preço de venda. A leitura de um
preço de custo menor do que 0 indica o fim da leitura dos dados.
2. Em uma lanchonete podem ser atendidas até 14 pessoas em um dia. Para cada cliente leia
seu nome, os itens e a quantidade para cada item.
OBS:
• Os itens possíveis e seu respectivo valor estão na seguinte tabela:
Especificação ---    preço unitário
Cachorro-quente (1)  RS 5,10
Hambúrguer      (2)  R$ 8,00
Refrigerante    (3)  R$ 2,55

Caso seja lida uma opção inválida (que não existe na tabela) deverá ser
informado ao usuário;
• Um cliente pode ter em um pedido vários itens, inclusive repetidos;
• Considere a palavra “NÃO” como o fim da leitura dos itens de um cliente.
Ao final da leitura dos itens de cada cliente informe o valor total a ser pago. Após ser
lido todos os pedidos dos clientes, escreva para o usuário o total arrecadado no dia.

PARA TESTA: 

Alfredo  
op 1 quant 4
op 2 quant 3
op 3 quant 2
op 1 qunt 1
op 2 qunt 3
total para ele = 78.60
Dayse
op 1 quant 4
op 2 quant 3
op 3 quant 2
para ela = 49.50
Verônica
op 1 quant 4
op 2 quant 3
total para ela = 44.40
Sabrina
op 1 qunt 1
op 2 qunt 3
total para ela = 29.10
Total geral =  201.60
'''
nomes = []
clientes = int(input('quantidade de clientes:'))
# variável global para todas 
total_apagar = 0
quantidades = 0
for i in range(clientes): #14
    nome = input('diga o nome do cliente :')
    p = ''
    produltos = []
    # variável individual aqui
    quantidades = 0
    total_individual = 0
    while p != 'não':
        print('='*40)
        print('Cachorro-quente (1)')
        print('Hambúrguer      (2)')
        print('Refrigerante    (3)')
        print('='*40)
        item = int(input('Pedido:'))
        quant = int(input('quantidade do item :'))
        print('='*10)
        if item == 1 :
            produlto = 'Cachorro-quente'
            preco = quant*5.10
            quantidades += 1
        elif item == 2:
            produlto = 'Hambúrguer'
            preco = quant*8.00
            quantidades += 1
        elif item == 3:
            produlto = 'Refrigerante'
            preco = quant*2.55
            quantidades += 1
        else:
            print('Opção inválida')    
        total_individual += preco
        if produlto not in produltos:
            produltos.append(produlto)
        print(f'nome do cliente : {nome}')
        print(f'lista de produto do cliente {produltos} quantidade de produto {quantidades} ')        
        print(f'TOTAL PARA ESSE CLIENTE R$ {total_individual:.2f}')
        p = input('deseja fazer outro pedido? use [não]_p/sair ou [s] p/continuar:')
        print('='*40)
    # total geral dentro do loop do for
    total_apagar += total_individual
    if nome not in nomes:
        nomes.append(nome)
print(f'Nomes dos clients {nomes}')
print(f'TOTAL A PAGAR R$ = {total_apagar:.2f}')

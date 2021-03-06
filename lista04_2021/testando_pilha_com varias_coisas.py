from time import sleep
pilha = []
pacotes = []
for s in range(10): # 10
    nome = input('digite o nome :')
    pilha.append(nome)
    print(f'tamanho da pilha = {len(pilha)}')
    print(f'topo da pilha = {pilha[-1]}')
    for x in pilha:
        print('elementos da pilha ',x)
    # desempacotar
        if nome not in pacotes:
            pacotes.append(nome)
            if len(pacotes) == 10:
                a = pacotes[0] , b = pacotes[1], c = pacotes[2], d = pacotes[3], e = pacotes[4], f = pacotes[5], g = pacotes[6],  h = pacotes[7], i = pacotes[8], j = pacotes[9] 
                desempacotando = a , b , c , d , e , f , g , h , i , j 
                print('desempacotando',desempacotando) 
    d = input('escreva [desep] para desempilhar ou [esva] p/esvaziala ou [cont]p/continuar: use [sair] p/encerra:')
    if d == 'sair':
        break
    if d == 'cont':
        pass
    desempilhar  = ''
    for elemento in pilha:
        sleep(2)
        print(f'Elementos da pilha  = {elemento}')
        if d == 'desep':
            if 0 < len(pilha):
                desempilhar = (pilha.pop())
                print(f'Desempilhando = {desempilhar}')
        if d == 'esva':
            if len(pilha) > 0 :
                print(f'pinha atual = {pilha}')

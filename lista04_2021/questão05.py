from time import sleep
pilha = []
for s in range(6): # 10
    nome = input('digite o nome ou [desep]/pra_desempinha, esvazi_p/esvaziar:')
    if nome != 'desep':
        if nome != 'esvazi':
            pilha.append(nome)
    print('pilha = ',pilha)
    # tamanho da pilha
    print(f'tamanho da pilha = {len(pilha)}')
    # topo da pilha 
    print(f'topo da pilha = {pilha[-1]}')
    # mostra elementos
    for elemento in pilha:
        print(f'elemento = {elemento}')
        sleep(1)
    if nome == 'esva':
        while len(pilha) >= 0:
            pilha.pop()
    # desempilhar
    desempilhar  = ''
    if nome == 'desep':
        pilha.pop()

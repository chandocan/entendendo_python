print('PROGRAMA PARA ADICIONA E REMOVER LIVROS')
adiciona = ''
pilha = []
x = None
while adiciona != 'sair':
    print('='*30)
    adiciona = input('nome do livro ou remove ou sair:').lower()
    if adiciona != 'sair':
        if adiciona != 'remove':
            pilha.append(adiciona)
    if adiciona == 'remove':
        x = pilha.pop( )
        if len(pilha) == 0:
            print('não existe livros')
            print('OBSERVAÇÃO ATENÇÃO')
            print('não use remove sem livros add mais livros')
    print('='*30)
    print(f'livro removido {x}')
    print(pilha)

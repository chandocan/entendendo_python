'''
Considerando uma matriz 4x4 preenchida com valores inteiros fixos,
Retorne a soma de cada linha e qual é a maior soma. 
'''
matriz = []
print('Informe números para compor uma matriz 4x4.')
for i in range(1,4+1):
    linha = []
    for j in range(1,4+1):
        num = int(input('Digite o elemento [%d][%d] da matriz: '%(i,j)))
        linha.append(num)
    matriz.append(linha)

linha = 1

print()
print("="*60) #só fez printa o sinal de igual 60 vezes

for x in range(len(matriz)):

    for y in range(len(matriz)):

        print(f'[{matriz[x][y]:^5}]', end='')
    print()

print("="*60)
print()

for valor in matriz:

    soma = 0
    cont = 0

    while(cont < len(matriz)):

        soma += valor[cont]
        cont += 1
    
    print(f'Soma da linha {linha} = {soma}')
    linha += 1

'''
matriz = []
print('Informe números para compor uma matriz 4x4.')
for i in range(1,4+1):
    linha = []
    for j in range(1,4+1):
        num = int(input('Digite o elemento [%d][%d] da matriz: '%(i,j)))
        linha.append(num)
    matriz.append(linha)

linha = 1

print(matriz)
print("="*60) # so fez repitir o igual 60 vezes para organizar
# assim a matriz é organizada em linhas e colunas
# fez uma interação entre a matriz é a varial x e a varia y do for 
# A função  len(len(matriz)) foi usado para ver o tamanho das linhas é colunas da matriz
for x in range(len(matriz)):

    for y in range(len(matriz)):

        print(f'[{matriz[x][y]:^5}]', end='')
    print()
for valor in matriz:

    soma = 0
    cont = 0

    while(cont < len(matriz)):

        soma += valor[cont]
        cont += 1
    
    print(f'Soma da linha {linha} = {soma}')
    linha += 1


'''
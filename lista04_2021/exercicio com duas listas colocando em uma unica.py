# 10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

primeiro_vetor = []
segundo_vetor = []
terceiro_vetor = []
# vai add em cada lista separada é depois vai add em uma lista os indices separados
for posicao in range(10):
    primeiro_vetor.append(input("Digite o elemento da "+str(posicao+1)+"ª posição do primeiro vetor: "))

for posicao in range(10):
    segundo_vetor.append(input("Digite o elemento da "+str(posicao+1)+"ª posição do segundo vetor: "))
    
for indice in range(10): # colocando duas lista de forma alternada 
    
    terceiro_vetor.append(primeiro_vetor[indice])
    terceiro_vetor.append(segundo_vetor[indice])
  
print(terceiro_vetor)

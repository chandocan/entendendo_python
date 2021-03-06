pilha = ["Gustavo", "Rafael", "Mariana", "Lucas", "Higor", "Juliana",
"Viviane", "Sávio", "Gabriel", "Paula"]
#letra a
pilha.append("Filipe")
pilha.append("Marcella")
#letra b
pilha.pop()
#letra c
print(len(pilha))
#letra d
print(pilha[-1])
#letra e
print(pilha[-2])
#letra f
print(pilha[0])
#letra g
print(pilha)
#letra h
n = int(input("Digite a quantidade de elementos:"))
if(n <= len(pilha)):
    for i in range(n):
        pilha.pop()
    else:
        print("N maior que a quantidade de elementos!")
    print(pilha)
#letra i
del pilha[0:]
print(pilha)
#ou
for i in range(len(pilha)):
    pilha.pop()
print(pilha)

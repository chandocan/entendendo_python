# dadoC for dadoA in iteravel :
# ONDE TENHO DADOC posso fazer uma multiplicação uma divisão ou mesmo equação qualquer coisa
# vai gera uma nova lista 
# obs DADOC é A MESMA lista


print("usou compreenção de lista")
lista = [1,2,3,4,5,6,7]

# listaI é o mesmo que lista de compreenção
# nome desse assunto em python list comprehension
# o interavel aqui é lista 
# o dado são os indeces dessa lista
res = [listaI * 10 for listaI in lista] # na verdade isso é um loop de uma unica linha
print(res)
print("A lista principal não foi modificada")
print(lista)

# obs antes do for pode receber uma função do python criada por você 
# com def nome_da_funcão():


# usando a logica com uma função
def soma(valor):
    soma = valor + 1
    return soma

res = [soma(listaI) for listaI in lista]
print("foi usado uma função ")
print(res)

# execultando letras em caixa alta

nome = "jose Alfredo"
print("Abaixo temos todas as letras do nome em caixa alta feito isso com uma linha")
print([letra.upper() for letra in nome])

# colocando os nomes da lista em caixa alta

def caixa_alta(nome):
    nome = nome.replace(nome[0:],nome[0:].upper())
    return nome

amigos = ['verônica','Dayse','sabrina','fernada']
print([caixa_alta(amigo) for amigo in amigos])


# outro jeito de fazer
amigos = ['karla','maria','jose']
# deixando caixa alta todos os nome da lista
# deixei no plural concatenando uma letra S
print([amigo[0:].upper()+"S" for amigo in amigos])

# trabalhando com boolean em python
# lembrando que o zero em python é false
# zero vazio em python é false
print([bool(valor) for valor in [0,[], '', True, 1, 3.14]])

#convertendo para string

print([str(numero) for numero in [1,2,3,4,5]])

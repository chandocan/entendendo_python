custo=0
cont=0
somacusto=0
somavenda=0
custo=float(input("digite o preço de custo: "))
while custo>=0:
    venda=float(input("digite o preço de venda: "))
    if custo>venda:
        print("Ouve um prejuzo de: ", custo-venda)
    somacusto=+custo
    somavenda=+venda
    cont=+1
    custo=float(input("digite o preço de custo: "))
print("A media do preço de venda é:",somavenda/cont,"A media do preço de custo é:",somacusto/cont)

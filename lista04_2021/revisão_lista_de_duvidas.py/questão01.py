soma_p_c = 0
soma_p_v = 0
soma_produlto = 0
p_custo = float(input('preço de custo:'))
#p_venda = float(input('preço de venda:'))
while p_custo >= 0:
    print('use preço de custo [-1] para sair')
    p_venda = float(input('preço de venda:'))
    if p_custo > p_venda:
        print(f'prejuízo R$ = {p_custo - p_venda:.2f}')
    else:
        print(f'lucro R$ = {p_venda - p_custo:.2f}')
    soma_p_c += p_custo
    soma_p_v += p_venda
    soma_produlto += 1
    p_custo = float(input('preço de custo:'))
    #p_venda = float(input('preço de venda:'))
print(f'media preço de custo R$ = {soma_p_c/soma_produlto:.2f}')
print(f'medida preço de venda R$ = {soma_p_v/soma_produlto:.2f}')

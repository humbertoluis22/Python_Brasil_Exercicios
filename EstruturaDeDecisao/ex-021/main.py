print('Caixa eletronico\n')

valor_saque = int(input('diite o valor do saque [10 - 600 ] : '))

if valor_saque < 10 or valor_saque > 600:
    print('Valor inválido')
else:
    nota_cem = valor_saque // 100
    nota_cinquenta =  (valor_saque % 100) // 50 

    print(nota_cem)
    print(nota_cinquenta)  

    #finalzar cofdigo
preco = float(input('Valor do produto: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA dinheiro/cheque
[ 2 ] À VISTA cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no nartão
''')
forma_pagamento =  int(input('Digite a forma de pagamento:'))
v = False
x = False
if forma_pagamento == 1:
    preco = preco - (preco*10/100)

elif forma_pagamento == 2:
    preco = preco - (preco*5/100)
    
elif forma_pagamento == 3:
    p = int(input('Em quantas parcelas:'))
    if p <= 2:
        v = True
        m = preco/p
    else:
        print('Operação negada\nO limite é de até 2 vezes. Tente Novamente')
        x = True


elif forma_pagamento == 4:
    p = int(input('Em quantas parcelas:'))
    preco = preco + (preco*20/100)
    m = preco/p
    v = True

if x == False:
    print('O valor total a ser pago é de R${:.2f}'.format(preco))

if v == True:
    print('Em {} parcelas de R${:.2f}, por mês'.format(p,m))
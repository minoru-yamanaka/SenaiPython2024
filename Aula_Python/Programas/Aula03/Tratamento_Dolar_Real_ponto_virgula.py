dinheiro = input('Digite seu dinheiro: ')

dinheiro_validar = dinheiro.replace(',','')
dinheiro_validar = dinheiro_validar.replace('.','')
if dinheiro_validar.isdecimal():
    dinheiro = dinheiro.replace(',','.')
    dinheiro = float(dinheiro)
    print('Você ganhou 10 reais e ficou com ', dinheiro + 10)
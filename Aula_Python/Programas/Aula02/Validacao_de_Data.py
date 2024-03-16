
'''
titulo = 'Validação de Data'
Data: 31/07/2023
Autor: Daniel
Descrição: Verifica se uma data é valida
'''
titulo = 'Validação de Data'
print('Bem vindo ao programa ' + titulo)

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

ano_bissexto = False

if ano % 4 == 0:
    if (ano % 100 == 0 and ano % 400 == 0) or (ano % 100 > 0):
        ano_bissexto = True

data_valida = False

if dia > 0 and mes > 0 and ano > 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            data_valida = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            data_valida = True
    elif mes == 2:
        if ano_bissexto:
            if dia <= 29:
                data_valida = True
        else:
            if dia <= 28:
                data_valida = True


if data_valida:
    print('Esta data é valida')
else:
    print('Esta data não é valida')
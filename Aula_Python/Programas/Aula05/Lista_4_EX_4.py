titulo = 'Validação 2 Digitos CPF'
'''
Data: 12/05/2023
Autor: Daniel
Descrição: Valida os 2 digitos do CPF
que o usuario digitou
'''
print('Seja bem vindo ao programa ' + titulo)

while True:
    cpf = input('Digite um CPF: ')

    if len(cpf) == 14:
        if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
            print('CPF inválido')
            continue
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

    if len(cpf) != 11 or not cpf.isdecimal():
        print('CPF inválido')
        continue

    print('CPF:', cpf)
    multiplicador = 10
    soma = 0
    for numero in cpf[0:9]:
        resultado = int(numero) * multiplicador
        soma += resultado
        print(numero, 'x', multiplicador, '=', resultado)
        multiplicador -= 1

    soma = soma * 10
    soma = soma % 11

    if soma > 9:
        soma = 0
    print('1 Digito CPF calculado:', soma)
    print('1 Digito CPF inserido:', cpf[9])
    if soma == int(cpf[9]):
        print('Primeiro Digito Verificador Válido')

        multiplicador = 11
        soma = 0
        for numero in cpf[0:10]:
            resultado = int(numero) * multiplicador
            soma += resultado
            print(numero, 'x', multiplicador, '=', resultado)
            multiplicador -= 1

        soma = soma * 10
        soma = soma % 11

        if soma > 9:
            soma = 0
        print('2 Digito CPF calculado:', soma)
        print('2 Digito CPF inserido:', cpf[10])
        if soma == int(cpf[10]):
            print('Segundo Digito Verificador Válido')
        else:
            print('CPF Inválido')
    else:
        print('CPF Inválido')
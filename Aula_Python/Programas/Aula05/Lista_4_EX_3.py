titulo = 'Validação 1º Digito CPF'
'''
Data: 29/04/2023
Autor: Daniel
Descrição: Valida o 1º digito do CPF
que o usuario digitou
'''
print('Seja bem vindo ao programa ' + titulo)

while True:
    # Passo 1: Pedir o CPF
    cpf = input('Digite um CPF: ')
    # Passo 1.5: Validar entrada
    # (veio só números?)
    # (se veio . e - estão na posição certa?)

    if not cpf.isdecimal():
        if not((cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-')) or len(cpf) != 14:
            print('CPF não númerico com caracteres em posições inválidas')
            continue
        cpf = cpf.replace('.','')
        cpf = cpf.replace('-', '')
    if not cpf.isdecimal():
        print('CPF inválido')
        continue
    if len(cpf) != 11:
        print('Tamanho do CPF inválido')
        continue

    # Passo 2: Fazer o calculo do indice x digito do cpf

    multiplicador = 10
    soma = 0

    for digito in cpf[:9]:
        # print(f'{digito} x {multiplicador} = {int(digito) * multiplicador}')
        soma += int(digito) * multiplicador
        multiplicador -= 1

    # # Usando list compreension
    # #  crie duas listas (iteraveis)
    # lista_1 = range(9) # lista de 0 a 8
    # lista_2 = range(10,1,-1) # lista de 10 a 2
    # # junte as listas indice a indice usando a função zip
    # lista_conjunta = zip(lista_1,lista_2)
    # # use list compreension com desempacotamento de duas variaveis
    # # multiplicando o cpf (usando o indice do cpf --> lista_1)
    # # com o multiplicador --> lista_2
    # lista_mult = [int(cpf[x]) * y for x,y in lista_conjunta]
    # # somar cada multiplicação usando a função soma
    # soma = sum(lista_mult)
    #
    # # tudo isso em 1 linha
    # # soma = sum([int(cpf[x])*y for x,y in  zip(range(9),range(10,1,-1))])

        # Passo 3: Multiplicar por 10
        soma *= 10
        # print(f'Mult * 10: {soma}')

        # Passo 4: Resto da divisão por 11
        soma = soma % 11
        # print(f'Resto: {soma}')

        # Passo 5: Verificar se o valor deu maior que 9
        # se sim mudar pra 0
        if soma > 9:
            soma = 0
        # print(f'Verificar > 9: {soma}')

        # Passo 6: Comparar digito calculado com o digito inserido
        # print(f'Calculado: {soma}  Inserido: {cpf[9]}')
        # print(f'Resultado: {soma == int(cpf[9])}')
        if soma == int(cpf[9]):
            print('CPF Válido')
            # break
        else:
            print('CPF Inválido')
            # break
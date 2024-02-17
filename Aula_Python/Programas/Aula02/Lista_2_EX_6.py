titulo = 'Ano Bissexto'
'''
Data: 02/05/2023
Autor: Daniel
Descrição: Verifica se um ano é bissexto
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe um ano')

ano = int(input())


# Validação no Formato 1
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        bissexto = False
    else:
        bissexto = True
else:
    bissexto = False

if bissexto == True:
    print('Ano Bissexto')
else:
    print('Não é Ano Bissexto')





# Validação no Formato 2
# primeiro if: anos 400 800 1200...
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    bissexto = True
# segundo if: anos 4 8 12... menos anos 100 200 300
elif ano % 4 == 0 and ano % 100 != 0:
    bissexto = True
else:
    bissexto = False

if bissexto == True:
    print('Ano Bissexto')
else:
    print('Não é Ano Bissexto')








# Validação no Formato 3
# Simplificação lógica: C + A.B/
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False

if bissexto == True:
    print('Ano Bissexto')
else:
    print('Não é Ano Bissexto')



# Validação no Formato 4
# Se baseando em algebra de Boole: A. ((B/.C/) + (B.C))
A = ano % 4 == 0
B = ano % 100 == 0
C = ano % 400 == 0

if A and ((not B and not C) or (B and C)):
    ano_bissexto = True
else:
    ano_bissexto = False

if bissexto == True:
    print('Ano Bissexto')
else:
    print('Não é Ano Bissexto')
titulo = 'Calculadora de Media de Notas'
'''
Data: 27/04/2023
Autor: Daniel
Descrição: Calcula a média de quatro notas
informadas pelo usuário
'''
print('Bem vindo ao programa ' + titulo)

nota_1 = float(input('Digite a 1ª nota do 1º Semestre: '))
nota_2 = float(input('Digite a 2ª nota do 1º Semestre: '))
nota_3 = float(input('Digite a 1ª nota do 2º Semestre: '))
nota_4 = float(input('Digite a 2ª nota do 2º Semestre: '))

media_1 = (nota_1 + nota_2) / 2
media_2 = (nota_3 + nota_4) / 2
media_final = (media_1 + media_2) / 2

print('Média do 1º Semestre: ' + str(media_1))
print('Média do 2º Semestre: ' + str(media_2))
print('Média Final: ' + str(media_final))
titulo = 'Jogo da Forca'
'''
Data: 29/07/2023
Autor: Daniel
Descrição: Jogo da Forca
'''
print('Bem vindo ao programa ' + titulo)


palavra_secreta = input('Digite a palavra/frase secreta: ').upper()
dica = input('Digite uma dica: ')

# Método 1 : Comparação de Indices

# palavra_jog = ''
#
# for letra_secreta in palavra_secreta:
#     if letra_secreta == ' ' or letra_secreta == '-':
#         palavra_jog += letra_secreta
#     else:
#         palavra_jog += '_'
#
# print('\n' * 50)
#
#
# print(f'Dica: {dica}')
#
# while True:
#     print(f'Palavra: {palavra_jog}')
#
#     letra_teste = input('Digite uma letra/número: ')
#
#     if letra_teste in palavra_secreta:
#         for indice_secreta, letra_secreta in enumerate(palavra_secreta):
#             palavra_temp = ''
#             if letra_secreta == letra_teste:
#                 for indice_jogador, letra_jogador in enumerate(palavra_jog):
#                     if indice_jogador == indice_secreta:
#                         palavra_temp += letra_secreta
#                     else:
#                         palavra_temp += letra_jogador
#                 palavra_jog = palavra_temp












# Método 2 : Usando o método de string replace


# palavra_jog = ''
#
# for letra_secreta in palavra_secreta:
#     if letra_secreta == ' ' or letra_secreta == '-':
#         palavra_jog += letra_secreta
#     else:
#         palavra_jog += '_'
#
# print('\n' * 50)
#
#
# print(f'Dica: {dica}')
#
# while True:
#     print(f'Palavra: {palavra_jog}')
#
#     letra_teste = input('Digite uma letra/número: ')
#
#     if letra_teste in palavra_secreta:
#         palavra_temp = palavra_secreta
#         for letra_temp in palavra_temp:
#             if letra_temp != letra_teste:
#                 if letra_temp not in palavra_jog:
#                     palavra_temp = palavra_temp.replace(letra_temp,'_')
#
#         palavra_jog = palavra_temp






# Método 3 : palavra jogador desorganizada e organizando no print

palavra_jog = ''

print('\n' * 50)


print(f'Dica: {dica}')

tentativas = 10
letras_testadas = ''

while True:
    print(f'Tentativas: {tentativas}')
    print('Palavra: ',end='')

    for letra_secreta in palavra_secreta:
        if letra_secreta == ' ' or letra_secreta == '-' or letra_secreta in palavra_jog:
            print(letra_secreta,end='')
        else:
            print('_',end='')
    print()

    ''' Imprimindo usando list compreension '''
    # print(*[letra_secreta
    #         if letra_secreta in (' ', '-', *(palavra_jog))
    #         else '_' for letra_secreta in palavra_secreta])

    letra_teste = input('Digite uma letra/número: ').upper()

    if len(letra_teste) > 1:
        print('Digite apenas uma letra ou número')
        continue
    if letra_teste in letras_testadas:
        print('Você já digitou esta letra/número')
        continue

    letras_testadas += letra_teste

    if letra_teste in palavra_secreta:
        if letra_teste not in palavra_jog:
            palavra_jog += letra_teste
    else:
        tentativas -= 1
        print(f'A letra {letra_teste} não existe na palavra')


    if tentativas <= 0:
        print(f'Você perdeu, a palavra era {palavra_secreta}')
        break

    venceu = True

    for letra_secreta in palavra_secreta:
        if letra_secreta != ' ' and letra_secreta != '-' and letra_secreta not in palavra_jog:
            venceu = False
            break

    ''' Verificando vitoria usando list compreension '''
    # venceu = len([True for letra in palavra_secreta
    # if (letra in palavra_jog)]) == len(palavra_secreta)

    if venceu:
        print('Palavra: ', end='')
        for letra_secreta in palavra_secreta:
            if letra_secreta == ' ' or letra_secreta == '-' or letra_secreta in palavra_jog:
                print(letra_secreta, end='')
            else:
                print('_', end='')
        print()
        print('Parabéns!!! Você venceu!')
        break

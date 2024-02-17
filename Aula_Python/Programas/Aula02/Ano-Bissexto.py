
# 6)Leia o texto abaixo sobre o Ano Bissexto:
# “O calendário gregoriano, estabelecido pela primeira vez em 1582 pelo Papa Gregório XIII, foi projetado para corrigir
# os erros introduzidos pelo calendário juliano, que é menos preciso.
# No calendário gregoriano, um ano normal consiste em 365 dias. Como o comprimento real de um ano sideral
# (o tempo necessário para a Terra girar uma vez sobre o Sol) é na verdade de 365,2425 dias, um "ano bissexto"# de 366
# dias é usado uma vez a cada quatro anos para eliminar o erro causado por três anos normais (mas curtos).
# Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos.
# No entanto, ainda há um pequeno erro que deve ser contabilizado. Para eliminar esse erro, o calendário gregoriano
# estipula que um ano que é uniformemente divisível por 100 (por exemplo, 1900) é um ano bissexto apenas se também
# é igualmente divisível por 400.
# Por essa razão, os seguintes anos não são bissextos:
# 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600:
# Isso porque eles são uniformemente divisíveis por 100, mas não por 400.
# Os seguintes anos são bissextos: 1600, 2000, 2400
# Isso porque eles são uniformemente divisíveis por 100 e 400.”
# Faça um programa no qual o usuário informe um ano e o sistema responda se o ano é bissexto ou não.

class AnoBissexto:
    def __init__(self):
        # Solicita ao usuário que informe um ano e converte a entrada para inteiro
        ano_informado = int(input("Informe o ano: "))

        # Verifica se o ano é bissexto e imprime a mensagem correspondente
        if ano_informado % 4 == 0 and (ano_informado % 100 != 0 or ano_informado % 400 == 0):

        # - ano_informado % 4 == 0: Isso verifica se o ano é divisível  por 4, pois os anos bissextos
        # geralmente têm essa  propriedade.
        # - ano_informado % 100 != 0: Este é um segundo critério para garantir que o ano não seja divisível
        # por 100, a menos que:
        # - ano_informado % 400 == 0: Se  o  ano for divisível por 100,
        # ele ainda pode ser bissexto se for divisível por 400.

            print(f"O ano {ano_informado} é bissexto.")
        else:
            print(f"O ano {ano_informado} não é bissexto.")
# call_AnoBissexto = AnoBissexto()

# 7)Faça um programa que pergunte uma data ao usuário (dia, mês e ano separadamente) e valide se aquela data é real ou não, fazendo as seguintes validações:
# •	Verificar se o dia informado existe dentro daquele mês
# o	Tem 31 dias se o mês for 1, 3, 5, 7, 8, 10 ou 12;
# o	Tem 30 dias se o mês for 4, 6, 9 ou 11;
# o	Tem 28 dias se o mês for 2 e o ano não for bissexto;
# o	Tem 29 dias se o mês for 2 e o ano for bissexto.
# •	Verificar se o mês informado existe (ano vai até 12 meses);
# •	Verificar se o dia, mês e ano são valores positivos.
# Informar ao usuário se a data for válida ou não.

class DataReal:
    def __init__(self):
        # Solicita ao usuário que informe o dia, mês e ano separadamente
        dia = int(input("Informe o dia: "))
        mes = int(input("Informe o mês: "))
        ano = int(input("Informe o ano: "))

        # Verifica se o ano é bissexto
        ano_bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

        # Verifica se o mês e o dia estão dentro dos limites
        if 1 <= mes <= 12 and 1 <= dia <= 31 and mes == 1 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 3 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 5 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 7 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 8 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 10 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 12 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 4 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 6 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 9 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 11 or \
                (ano_bissexto and 1 <= dia <= 29 and mes == 2) or \
                (not ano_bissexto and 1 <= dia <= 28 and mes == 2):
            print("Data válida!")
        else:
            print("Data inválida!")
class_DataReal = DataReal()

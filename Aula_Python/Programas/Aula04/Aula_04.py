# # 1)Para a str a seguir:
# # jose
# # jorge
# # maria
# # antonio
# # ana
# # julia
# # márcio
# # fernando
# # zelia
#
# lista = '''jose
# jorge
# maria
# antonio
# ana
# julia
# márcio
# fernando
# zelia
# '''
#
# # Faça um programa para imprimir estes dados com os índices de cada um.
# # Exemplo:
# # 1 – jose
# # 2 – jorge
# # 3 – maria
#
# # Nomes, imprimindo-os com seus índices
# for indice, lista in enumerate(lista, start=1):
#     print( str(indice) + '-' + str(lista))
import time

# 2) Crie um programa para inserir, apagar e listar os itens de uma lista de compras (utilize append e pop/del).

while True:
    lista = ['banana','maçã','lichia','pessêgo']
    print('Esta é a lista de compras: ',lista)
    print('-'*20)


    print('''Você quer add mais um item?
    Escolha uma opção:
    (S) --> Sim
    (N) --> Não
    (R) --> Remover
    ''')
    escolha = input('Opção: ').upper()

    if escolha not in ('S','N','R'):
        print('Opção inválida')
        time.sleep(1)
        continue
    elif escolha == 'S':
        time.sleep(0.5)
        adicionar = str(input('Insira um item na lista: '))
        lista.append(adicionar)
        print(lista)
    elif escolha == 'R':
        time.sleep(0.5)
        remove = int(input('Remova um item na lista: '))
        lista.remove(adicionar)
        print(lista)
    elif escolha == 'N':
        time.sleep(0.5)
        break




    else:
        pass




# 3)	Faça um programa que o usuário digite um CPF (exemplo: 123.456.789-10) e o sistema valide se o primeiro digito verificador está correto (no caso do exemplo, o número 1 após o traço).
# Para validar este dígito verificador deve seguir os seguintes passo:
# 1.	Multiplicar cada número do CPF por um valor respectivo:
# Ex: CPF 132.465.987-10
#
# 1      3      2      4      6      5      9      8      7
# X
# 10    9      8      7      6      5      4      3      2
# =
# 10   27    16    28    36     25   36    24    14
#
# 2.	Somar os resultados:
#
# 10 + 27 + 16 + 28 + 36 + 25 + 36 + 24 + 14 = 216
#
# 3.	Multiplicar o resultado por 10:
#
# 216 x 10 = 2160
#
# 4.	Obter o resto da divisão do valor por 11:
#
# 2160 % 11 = 4
#
# 5.	Se o resultado anterior for maior que 9 o resultado é 0, se não o resultado anterior é o resultado (no exemplo: 4)
#
# 6.	Se o Resultado for igual ao primeiro dígito verificador está correto, senão está incorreto
# CPF  do exemplo: 132.465.987-10
# 1º Digito verificador: 1
# Resultado do cálculo: 4
# Logo:
# CPF inválido
#
# 4)	Faça um programa que o usuário digite um CPF (exemplo: 123.456.789-10) e o sistema valide se os dois dígitos verificadores estão corretos (no caso do exemplo, o número 4 e número 0 após o traço).
#
# Para validar o primeiro dígito, siga o exemplo executado no exercício 3.
#
# Para validar o segundo dígito verificador deve seguir os seguintes passo:
# 1.	Multiplicar cada número por um valor respectivo + o primeiro dígito verificador:
# Ex: CPF 132.465.987-46
# 1      3      2      4      6      5      9      8      7       4
# X
# 11    10    9      8      7      6      5      4      3       2
# =
# 11     30   18    32    42    30    45    32    21     8
#
# 2.	Somar os resultados:
#
# 11 + 30 + 18 + 32 + 42 + 30 + 45 + 32 + 21 + 8 = 269
#
# 3.	Multiplicar o resultado por 10:
#
# 269 x 10 = 2690
#
# 4.	Obter o resto da divisão do valor por 11:
#
# 2690 % 11 = 6
#
# 5.	Se o resultado anterior for maior que 9 o resultado é 0, se não o resultado anterior é o resultado (no exemplo: 6)
#
# 6.	Se o Resultado for igual ao segundo dígito verificador está correto, senão está incorreto
# CPF  do exemplo: 132.465.987-46
# 2º Digito verificador: 6
# Resultado do cálculo: 6
# Logo:
# CPF válido

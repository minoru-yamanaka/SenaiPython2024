# import random
#
# resultados = [0, 0, 0, 0, 0, 0]
#
# for i in range(1000):
#     dado = random.randint(1, 6)
#     resultados[dado - 1] += 1
# for indice, resultado in enumerate(resultados):
#     print(f' {indice + 1}: {resultado}')

# import random
#
# resultados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# for i in range(1000):
#     dado1 = random.randint(1, 6)
#     dado2 = random.randint(1, 6)
#
#     resultados[dado1 + dado2 - 2] += 1
# for indice, resultado in enumerate(resultados):
#     print(f' {indice + 2}: {resultado}')

import random
dados = int(input('Insira o número de dados: '))
n_resultados = 5 * dados +1
resultados = [0]*n_resultados
vezes = int(input("Insira o n de vezes q quer lançar os dados: "))

for i in range(vezes):
    soma = 0
    for j in range(dados):
        soma += random.randint( 1,6)
    resultados[soma - dados] +=1

for indice, resultado in enumerate(resultados):
    print(f' {indice + dados}: {resultado}')

import random
class Lance:
    def __init__(self):
        # Define o número de lançamentos
        lancamentos = int(input("Digite o número de lançamentos: "))

        # Inicializa as variáveis para armazenar as ocorrências de soma de 2 a 12
        ocorrencia_2 = ocorrencia_3 = ocorrencia_4 = ocorrencia_5 = ocorrencia_6 = 0
        ocorrencia_7 = ocorrencia_8 = ocorrencia_9 = ocorrencia_10 = ocorrencia_11 = ocorrencia_12 = 0

        # Simula o lançamento dos dados n vezes
        for _ in range(lancamentos):
            # Obtém a soma dos dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            soma = dado1 + dado2
            # Incrementa a contagem da soma correspondente
            if soma == 2:
                ocorrencia_2 += 1
            elif soma == 3:
                ocorrencia_3 += 1
            elif soma == 4:
                ocorrencia_4 += 1
            elif soma == 5:
                ocorrencia_5 += 1
            elif soma == 6:
                ocorrencia_6 += 1
            elif soma == 7:
                ocorrencia_7 += 1
            elif soma == 8:
                ocorrencia_8 += 1
            elif soma == 9:
                ocorrencia_9 += 1
            elif soma == 10:
                ocorrencia_10 += 1
            elif soma == 11:
                ocorrencia_11 += 1
            elif soma == 12:
                ocorrencia_12 += 1

        # Mostra os resultados
        print(f"Número de lançamentos: {lancamentos}")
        print(f"Soma 2: {ocorrencia_2} ocorrências")
        print(f"Soma 3: {ocorrencia_3} ocorrências")
        print(f"Soma 4: {ocorrencia_4} ocorrências")
        print(f"Soma 5: {ocorrencia_5} ocorrências")
        print(f"Soma 6: {ocorrencia_6} ocorrências")
        print(f"Soma 7: {ocorrencia_7} ocorrências")
        print(f"Soma 8: {ocorrencia_8} ocorrências")
        print(f"Soma 9: {ocorrencia_9} ocorrências")
        print(f"Soma 10: {ocorrencia_10} ocorrências")
        print(f"Soma 11: {ocorrencia_11} ocorrências")
        print(f"Soma 12: {ocorrencia_12} ocorrências")

        # Encontra a soma que mais cai
        max_ocorrencia = max(ocorrencia_2, ocorrencia_3, ocorrencia_4, ocorrencia_5, ocorrencia_6,
                             ocorrencia_7, ocorrencia_8, ocorrencia_9, ocorrencia_10, ocorrencia_11, ocorrencia_12)
        soma_mais_frequente = []
        if max_ocorrencia == ocorrencia_2:
            soma_mais_frequente.append(2)
        if max_ocorrencia == ocorrencia_3:
            soma_mais_frequente.append(3)
        if max_ocorrencia == ocorrencia_4:
            soma_mais_frequente.append(4)
        if max_ocorrencia == ocorrencia_5:
            soma_mais_frequente.append(5)
        if max_ocorrencia == ocorrencia_6:
            soma_mais_frequente.append(6)
        if max_ocorrencia == ocorrencia_7:
            soma_mais_frequente.append(7)
        if max_ocorrencia == ocorrencia_8:
            soma_mais_frequente.append(8)
        if max_ocorrencia == ocorrencia_9:
            soma_mais_frequente.append(9)
        if max_ocorrencia == ocorrencia_10:
            soma_mais_frequente.append(10)
        if max_ocorrencia == ocorrencia_11:
            soma_mais_frequente.append(11)
        if max_ocorrencia == ocorrencia_12:
            soma_mais_frequente.append(12)

        print(f"A soma que mais cai é {soma_mais_frequente} ({max_ocorrencia} ocorrências)")

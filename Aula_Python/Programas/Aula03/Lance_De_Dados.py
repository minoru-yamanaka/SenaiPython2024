import random

class lance:
    def __init__(self):
        # biblioteca random para gerar números aleatórios

        # Define o número de lançamentos
        lancamentos = int(input("Digite o número de lançamentos: "))

        # Cria um dicionário para armazenar as ocorrências
        ocorrencias = {}
        for soma in range(1, 13):
            ocorrencias[soma] = 0

        # Simula o lançamento dos dados n vezes
        for _ in range(lancamentos):
            # Obtém a soma dos dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            soma = dado1 + dado2
            # Incrementa a contagem da soma no dicionário
            ocorrencias[soma] += 1

        # Mostra os resultados
        for soma, contagem in ocorrencias.items():
            print(f"Soma {soma}: {contagem} ocorrências")

        # Mostra o número que mais cai
        maior_contagem = max(ocorrencias.values())
        soma_mais_frequente = [soma for soma, contagem in ocorrencias.items() if contagem == maior_contagem]
        print(f"A soma que mais cai é {soma_mais_frequente} ({maior_contagem} ocorrências)")
call_lance = lance()
# 2) Crie um programa para inserir, apagar e listar os itens de uma lista de compras (utilize append e pop/del).
import time

lista_original = ['banana','maçã','lichia','pessêgo']
lista = lista_original.copy()  # Copiando a lista original

# Inicializando a lista de compras
lista_original = ['banana', 'maçã', 'lichia', 'pêssego']
lista = lista_original.copy()  # Copiando a lista original

while True:
    print('-' * 20)
    print('Esta é a lista de compras: ', lista)

    # Solicitando a escolha do usuário
    print('''Você quer adicionar ou remover um item?
Escolha uma opção:
(S) --> Adicionar
(R) --> Remover
(N) --> Não
''')
    escolha = input('Opção: ').upper()

    # Verificando a opção escolhida pelo usuário
    if escolha == 'S':
        adicionar = input('Insira um item na lista: ').lower()
        lista.append(adicionar)  # Adicionando o item à lista
        print(lista)

    elif escolha == 'R':
        remover = input('Remova um item da lista: ').lower()
        if remover in lista:
            lista.remove(remover)  # Removendo o item da lista
            print(lista)
        else:
            print("Item não encontrado na lista")

    elif escolha == 'N':
        break  # Saindo do loop

    else:
        print('Opção inválida')
        time.sleep(1)

print("Lista original:", lista_original)  # Imprimindo a lista original
print("Lista modificada:", lista)  # Imprimindo a lista modificada


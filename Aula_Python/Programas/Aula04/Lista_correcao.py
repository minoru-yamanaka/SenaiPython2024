lista_de_compras = []

while True:
    print('''Escolha uma opção:
(I) --> Inserir
(D) --> Deletar
(A) --> Atualizar
(L) --> Listar
(X) --> Sair''')
    escolha = input('Escolha: ').upper()

    if escolha not in ('I', 'A', 'D', 'L', 'X'):
        print('Escolha inválida')
        continue
    elif escolha == 'X':
        print('Saindo do programa')
        break
    elif escolha == 'I':
        while True:
            item = input('Digite o item a ser inserido ou S para Sair: ').upper()
            if item == 'S':
                break
            if item in lista_de_compras:
                print('Item já cadastrado')
                continue
            lista_de_compras.append(item)
            print(f'Item {item} inserido com sucesso')
    elif escolha == 'A':
        if len(lista_de_compras) == 0:
            print('Não tem itens na lista de compras')
        else:
            print('Escolha um item para atualizar')
            print('Lista de Compras')
            print('#' * 40)
            for numero, compra in enumerate(lista_de_compras, start=1):
                print(f'{numero} - {compra}')
            print('#' * 40 + '\n')

            num_atualizar = int(input('Número: '))
            valor_atualizado = input('Novo nome do item: ').upper()
            lista_de_compras[num_atualizar-1] =  valor_atualizado
            print(f'Item {valor_atualizado} atualizado com sucesso')
    elif escolha == 'D':
        if len(lista_de_compras) == 0:
            print('Não tem itens na lista de compras')
        else:
            print('Escolha um item pra deletar')
            print('Lista de Compras')
            print('#' * 40)
            for numero, compra in enumerate(lista_de_compras, start=1):
                print(f'{numero} - {compra}')
            print('#' * 40 + '\n')

            num_deletado = int(input('Número: '))
            item_deletado = lista_de_compras.pop(num_deletado-1)
            print(f'Item {item_deletado} deletado com sucesso')
    elif escolha == 'L':
        if len(lista_de_compras) == 0:
            print('Não tem itens na lista de compras')
        else:
            print('Lista de Compras')
            print('#'*40)
            for numero, compra in enumerate(lista_de_compras, start=1):
                print(f'{numero} - {compra}')
            print('#'*40 + '\n')
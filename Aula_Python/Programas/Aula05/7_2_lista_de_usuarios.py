import re


# Função para validar CPF
def validar_cpf(cpf):
    """
    Esta função valida um CPF fornecido.

    Args:
        cpf (str): O CPF a ser validado.

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    cpf = re.sub(r'[^0-9]', '', cpf)  # Remove caracteres não numéricos do CPF
    if len(cpf) != 11 or cpf == cpf[0] * 11:  # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))  # Calcula o primeiro dígito verificador
    digito1 = 11 - (soma % 11) if soma % 11 > 9 else 0
    if int(cpf[9]) != digito1:  # Verifica o primeiro dígito verificador
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))  # Calcula o segundo dígito verificador
    digito2 = 11 - (soma % 11) if soma % 11 > 9 else 0
    if int(cpf[10]) != digito2:  # Verifica o segundo dígito verificador
        return False

    return True


# Função para cadastrar usuário
def cadastrar_usuario(lista_usuarios):
    """
    Esta função permite ao usuário cadastrar um novo usuário.

    Args:
        lista_usuarios (list): A lista de usuários onde o novo usuário será adicionado.
    """
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    cpf = input("Digite o CPF do usuário: ")
    if validar_cpf(cpf):  # Valida o CPF fornecido
        usuario = {'nome': nome, 'idade': idade, 'cpf': cpf}
        lista_usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF inválido! Usuário não cadastrado.")


# Função para listar usuários
def listar_usuarios(lista_usuarios):
    """
    Esta função lista todos os usuários cadastrados.

    Args:
        lista_usuarios (list): A lista de usuários a ser listada.
    """
    if lista_usuarios:
        print("\nLista de Usuários:")
        for usuario in lista_usuarios:
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, CPF: {usuario['cpf']}")
    else:
        print("Nenhum usuário cadastrado.")


# Função para excluir usuário
def excluir_usuario(lista_usuarios):
    """
    Esta função permite ao usuário excluir um usuário existente.

    Args:
        lista_usuarios (list): A lista de usuários onde o usuário será excluído.
    """
    if lista_usuarios:
        cpf = input("Digite o CPF do usuário a ser excluído: ")
        for usuario in lista_usuarios:
            if usuario['cpf'] == cpf:
                lista_usuarios.remove(usuario)
                print("Usuário excluído com sucesso!")
                return
        print("Usuário não encontrado.")
    else:
        print("Nenhum usuário cadastrado.")


# Lista de usuários
usuarios = []

# Menu principal
while True:
    print("\nMenu:")
    print("1. Adicionar usuário")
    print("2. Excluir usuário")
    print("3. Listar usuários")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario(usuarios)
    elif opcao == '2':
        excluir_usuario(usuarios)
    elif opcao == '3':
        listar_usuarios(usuarios)
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

import re


def valida_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 11 or cpf == cpf[0] * 11:  # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    digito1 = resto if resto < 10 else 0
    if int(cpf[9]) != digito1:
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    digito2 = resto if resto < 10 else 0
    if int(cpf[10]) != digito2:
        return False

    return True


def cadastra_usuario(lista_usuarios, nome, idade, cpf):
    if valida_cpf(cpf):
        usuario = {'nome': nome, 'idade': idade, 'cpf': cpf}
        lista_usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF inválido. Cadastro não realizado.")


def exclui_usuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf:
            lista_usuarios.remove(usuario)
            print("Usuário excluído com sucesso!")
            return
    print("CPF não encontrado. Nenhum usuário excluído.")


def lista_usuarios(lista_usuarios):
    if lista_usuarios:
        for usuario in lista_usuarios:
            print("Nome:", usuario['nome'])
            print("Idade:", usuario['idade'])
            print("CPF:", usuario['cpf'])
            print("--------------------")
    else:
        print("Nenhum usuário cadastrado.")


# Exemplo de uso:
lista_de_usuarios = []

cadastra_usuario(lista_de_usuarios, "João", 25, "12345678901")
cadastra_usuario(lista_de_usuarios, "Maria", 30, "98765432109")
cadastra_usuario(lista_de_usuarios, "Pedro", 35, "12345678900")

print("Lista de usuários:")
lista_usuarios(lista_de_usuarios)

exclui_usuario(lista_de_usuarios, "12345678901")

print("Lista de usuários após exclusão:")
lista_usuarios(lista_de_usuarios)

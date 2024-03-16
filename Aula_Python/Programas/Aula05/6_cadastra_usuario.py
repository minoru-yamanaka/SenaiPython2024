def cadastra_usuario(lista_usuarios):
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    usuario = {'nome': nome, 'idade': idade}
    lista_usuarios.append(usuario)

# Exemplo de uso:
lista_de_usuarios = []
cadastra_usuario(lista_de_usuarios)
print(lista_de_usuarios)  # Saída: [{'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}]

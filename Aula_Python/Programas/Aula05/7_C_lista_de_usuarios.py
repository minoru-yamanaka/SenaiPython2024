# https://colab.research.google.com/drive/1uJvFWercMhxIA-RADamaBoukYq2MzR3b?usp=sharing

# Passo 1: Criar uma lista de usuarios vazia

lista_usuarios = []

# Função de validar CPF
def validar_cpf(cpf, digito=1):
  try:
    if len(cpf) == 14:
      if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

    if len(cpf) != 11:
      return False

    if not cpf.isdecimal():
      return False

    cursor_cpf = 0
    soma = 0
    for num_mult in range(9+digito, 1, -1):
      soma += num_mult * int(cpf[cursor_cpf])
      cursor_cpf += 1

    digito_teste = soma * 10

    digito_teste = digito_teste % 11

    if digito_teste > 9:
      digito_teste = 0

    if digito_teste == int(cpf[8+digito]):
      if digito == 1:
        return validar_cpf(cpf, digito=2)
      else:
        return True
    else:
      return False
  except BaseException as e:
    print(f'Erro ao validar CPF: {e}')
    return False

# Função validar usuario
def validar_usuario(nome, idade, cpf):
  if len(nome) == 0:
    return {'valido': False, 'valor': "Nome incorreto (vazio)"}

  if not idade.isdecimal():
    return {'valido': False, 'valor': "Idade com valor incorreto"}

  if not validar_cpf(cpf):
    return {'valido': False, 'valor': "CPF Inválido"}

  return {'valido': True, 'valor': ""}

# Função de cadastrar usuário

def inserir_usuario():
  try:
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    cpf = input('Digite seu CPF: ')
    usuario_validado = validar_usuario(nome, idade, cpf)
    if not usuario_validado['valido']:
      return usuario_validado['valor']

    idade = int(idade)


    ja_cadastrado = False
    for usuario in lista_usuarios:
      if cpf == usuario['cpf']:
        return "CPF já cadastrado anteriormente"

    if len(cpf) == 11:
      cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

    usuario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf
    }
    lista_usuarios.append(usuario)
    return f"Usuario {usuario['nome']} cadastrado com sucesso"
  except BaseException as e:
    return f'Erro ao Inserir usuário: {e}'

# Função de Listar Usuários

def listar_usuarios():
  try:
    if len(lista_usuarios) == 0:
      print('Lista de Usuário Vazia')
    else:
      print('#'*28 + 'USUARIOS' + '#'*28)
      print(f'{"#":^5} | {"Nome":^30} | {"Idade":^5} | {"CPF":^14}')
      for indice, usuario in enumerate(lista_usuarios, start=1):
        print(f'{indice:^5} | {usuario["nome"]:^30} | {usuario["idade"]:^5} | {usuario["cpf"]:^14}')
  except BaseException as e:
    return f'Erro ao Inserir usuário: {e}'

# Função de Atualizar Usuário

def atualizar_usuario():
  try:
    listar_usuarios()

    if len(lista_usuarios) > 0:
      indice_atualizar = int(input('Digite o código do usuário para atualizar: '))
      usuario_atual = lista_usuarios[indice_atualizar - 1]
      while True:
        print('Escolha o campo a ser atualizado: ')
        for key in usuario_atual.keys():
          print(key)

        campo = input('Digite o campo a ser atualizado: ').lower()

        novo_valor = input('Digite a atualização: ')
        usuario_atualizado = usuario_atual

        for key, value in usuario_atual.items():
          if key == campo:
            if type(key) == int:
              usuario_atualizado[key] = int(novo_valor)
            else:
              usuario_atualizado[key] = novo_valor

        usuario_validado = validar_usuario(usuario_atualizado['nome'], usuario_atualizado['idade'], usuario_atualizado['cpf'])
        if not usuario_validado['valido']:
          return usuario_validado['valor']

        lista_usuarios.pop(indice_atualizar-1)
        lista_usuarios.insert(indice_atualizar-1, usuario_atualizado)

        return f"Usuario {usuario_atualizado['nome']} atualizado com sucesso"

  except BaseException as e:
      return f"Erro ao atualizar Usuário? {e}"

# Função de Deletar Usuário

def deletar_usuario():
  try:
    listar_usuarios()

    if len(lista_usuarios) > 0:
      indice_deletar = int(input('Digite o código do usuário para deletar: '))
      confirmar = input(f'Você tem certeza que quer deletar o {lista_usuarios[indice_deletar-1]["nome"]}? (S ou N): ').upper()
      if confirmar == 'S':
        deletado = lista_usuarios.pop(indice_deletar-1)
        return f"Usuário {deletado['nome']} deletado com sucesso"
      else:
        return f"Usuário {lista_usuarios[indice_deletar-1]['nome']} não foi deletado"
    else:
      return ""
  except BaseException as e:
    return "Erro ao deletar usuário"

# Passo 2: Fazer um sistema de escolhas

while True:
  print('''Escolha uma opção:
(I) --> Inserir usuário
(D) --> Deletar usuário
(L) --> Listar usuários
(A) --> Atualizar usuário
(X) --> Sair''')
  escolha = input('Opção: ').upper()

  if escolha not in ('I', 'D', 'L', 'A', 'X'):
    print('Escolha inválida')
    continue
  elif escolha == 'X':
    print('Saindo do programa')
    break
  elif escolha == 'I':
    print(inserir_usuario())
  elif escolha == 'D':
    print(deletar_usuario())
  elif escolha == 'L':
    listar_usuarios()
  elif escolha == 'A':
    print(atualizar_usuario())
  print('#'*64 + '\n')
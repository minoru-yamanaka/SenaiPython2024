nome = 'Daniel'
idade = 30

print('Ola ' + nome + ', você tem ' + str(idade))
print('Ola ', nome, ', você tem ', '{:.2f}'.format(idade).replace('.',','),sep='')

print('Ola %s, você tem %d' % (nome, idade))
print('Ola %(vai_receber_nome)s, você tem %(idade_usuario)d' % { 'idade_usuario': idade, 'vai_receber_nome': nome})

print('Ola {}, você tem {}'.format(nome, idade))
print('Ola {1}, você tem {0}'.format(idade, nome))
print('Ola {vai_receber_nome}, você tem {idade_usuario}'.format(idade_usuario=idade, vai_receber_nome=nome))

dinheiro = 22.551561313
print('Você tem R$%.2f'%(dinheiro))
print('Você tem R$%(money).2f' % {'money': dinheiro})

print('Você tem R${:.2f}'.format(dinheiro))
print('Você tem R${money:.2f}'.format(money=dinheiro))

print('Eu ganhei {:.0%} desconto'.format(0.2))
print('Ola {:>50} você tem {} anos'.format(nome,idade))

print(f'Ola {nome:^30}, voce tem {idade:.2f} anos')

#-----------------------------------------------------

nome = 'Daniel'
idade = 30
dinheiro = 22.551561313

# Sem formatação usando casting
print('Ola ' + nome + ', você tem ' + str(idade))

# Separando objetos
print('Ola ', nome, ', você tem ', '{:.2f}'.format(idade).replace('.',','),sep='')

# Formatação Old Style %
print('Ola %s, você tem %d' % (nome, idade))
print('Ola %(vai_receber_nome)s, você tem %(idade_usuario)d' % { 'idade_usuario': idade, 'vai_receber_nome': nome})
print('Você tem R$%.2f'%(dinheiro))
print('Você tem R$%(money).2f' % {'money': dinheiro})

# Formatação New Style .format
print('Ola {}, você tem {}'.format(nome, idade))
print('Ola {1}, você tem {0}'.format(idade, nome))
print('Ola {vai_receber_nome}, você tem {idade_usuario}'.format(idade_usuario=idade, vai_receber_nome=nome))
print('Você tem R${:.2f}'.format(dinheiro))
print('Você tem R${money:.2f}'.format(money=dinheiro))
print('Eu ganhei {:.0%} desconto'.format(0.2))
print('Ola {:>50} você tem {} anos'.format(nome,idade))

# Usando f strings
print(f'Ola {nome}, você tem {idade}')
print(f'Você tem R${dinheiro:.2f}')
print(f'Você tem R${dinheiro:.2f}')
print(f'Eu ganhei {0.2:.0%} desconto')
print(f'Ola {nome:^50} você tem {idade} anos')
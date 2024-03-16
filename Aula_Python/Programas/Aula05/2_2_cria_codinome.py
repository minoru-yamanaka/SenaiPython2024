titulo = 'Criação de Digimon'

'''
Data: 12/05/2023
Autor: Daniel
Descrição: Retorna os primeiros 4 digitos do nome
junto com a palavra mon (EX: Daniel --> Danimon)
'''
print('Seja bem vindo ao programa ' + titulo)
def digimon(nome):
    if type(nome) != str:
        print('Chamada da função digimon inválida')
        print(f'Argumento "{type(nome)}" não pode ser utilizado')
    else:
        if not nome.isalpha():
            print('Chamada da função digimon inválida')
            print(f'Argumento str com valor "{nome}" inválido')
        else:
            print(nome[:4] + 'mon')

def digimon(nome):
    if type(nome) != str:
        print('Chamada da função digimon inválida')
        print(f'Argumento "{type(nome)}" não pode ser utilizado')
    else:
        if not nome.isalpha():
            print('Chamada da função digimon inválida')
            print(f'Argumento str com valor "{nome}" inválido')
        else:
            print(nome[:4] + 'mon')

print('Por favor, digite seu nome')
# tentativas de input
digimon(123)
digimon(['abc','def'])
digimon('daniel2')
nome = input('Nome: ')
# Insira seu nome
digimon(nome)
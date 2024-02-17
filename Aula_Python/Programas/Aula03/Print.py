import random

class Dado:
    def __init__(self):
        dado = random.randint(1, 6)
        print("O dado caiu em: " + str(dado))

# call_Dado = Dado()

# exemplo

class Contando:
        def __init__(self):

            for i in range(10):
                print(i)

# call_Contando = Contando()
class Contando2:
    def __init__(self):
        for i in 'Minoru':
            print(i)

# call_Contando = Contando2()

class Soma:
    def __init__(self):
        print('Quanto é 2 + 2?')
        valor = int(input())

        while valor != 4:
            print('errou')
            print('Quanto é 2 + 2?')
            valor = int(input())
        else:
            print('Certa a resposta')
# call_soma = Soma()

class Um_a_cem:
        def __init__(self):
            i = 0
            while i < 100:
                print(i)
                i += 1
                print(i)
# call_Um_a_cem = Um_a_cem()

class Senha:
        def __init__(self):
            print('Insira a senha: ')
            senha = input()

            while senha != 'a senha':
                print('Senha incorreta, tente novamente')
            else:
                print('Acesso liberado')
# call_senha = Senha()

class Eterno:
        def __init__(self):
            import time
            print('Este programa ai executar para sempre!')
            i = 0

            while True:
                print('Númeor de ciclos: ' + str(i))
                i +=1
                time.sleep(1)
# call_eterno = Eterno()

class chave:
        def __init__(self):
            print('Insira a senha: ')
            senha = input()

            print('Insira a senha para acessar: ')
            validar_senha = input()

            tent = 0

            while tent < 3:
                if senha != validar_senha:
                    tent += 1
                    print('Senha incorreta')
                    validar_senha = input('Digite novamnete a senha: ')
                else:
                    print('Acesso liberado')
                    break
            else:
                print('Errou o máximo de vezes')

# call_senha = chave()

class Senha3:
    def __init__(self):
        print('Digite a senha: ')
        tent = 1
        while tent <3:
            if senha != 'a senha':
                tent +=1
                print('Senha incorreta')
                senha = input('Digite a senha: ')
            else:
                print('Acesso liberado')
                break
        else:
            print('Errou o máximo de vezes')
# call_senha = Senha3()


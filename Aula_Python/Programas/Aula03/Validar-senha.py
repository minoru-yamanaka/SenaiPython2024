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
call_senha = Senha3()

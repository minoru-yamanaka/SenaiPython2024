class NotasAluno:
    def __init__(self):
        print('Insira a 1° nota do semestre: ')
        n1 = input()
        int(n1)
        print('Insira a 2° nota do semestre: ')
        n2 = input()
        r = int(n1) + int(n2)
        mediaFinal = r // 2

        if mediaFinal < 5:
            print('Este o aluno está Reprovado')
        elif mediaFinal > 7:
            print('Este o aluno está Aprovado')
        else:
            print('Este o aluno está de Recuperação')

call_NotasAluno = NotasAluno()
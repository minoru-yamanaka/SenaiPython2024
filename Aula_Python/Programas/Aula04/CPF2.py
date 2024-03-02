# 4)	Faça um programa que o usuário digite um CPF (exemplo: 123.456.789-10) e o sistema valide se os dois dígitos verificadores estão corretos (no caso do exemplo, o número 4 e número 0 após o traço).
#
# Para validar o primeiro dígito, siga o exemplo executado no exercício 3.
#
# Para validar o segundo dígito verificador deve seguir os seguintes passo:

# 1. Multiplicar cada número por um valor respectivo + o primeiro dígito verificador:
# Ex: CPF 132.465.987-46
# 1      3      2      4      6      5      9      8      7       4
# X
# 11    10    9      8      7      6      5      4      3       2
# =
# 11     30   18    32    42    30    45    32    21     8
#
# 2.	Somar os resultados:
#
# 11 + 30 + 18 + 32 + 42 + 30 + 45 + 32 + 21 + 8 = 269
#
# 3.	Multiplicar o resultado por 10:
#
# 269 x 10 = 2690
#
# 4.	Obter o resto da divisão do valor por 11:
#
# 2690 % 11 = 6
#
# 5.	Se o resultado anterior for maior que 9 o resultado é 0, se não o resultado anterior é o resultado (no exemplo: 6)
#
# 6.	Se o Resultado for igual ao segundo dígito verificador está correto, senão está incorreto
# CPF  do exemplo: 132.465.987-46
# 2º Digito verificador: 6
# Resultado do cálculo: 6
# Logo:
# CPF válido

cpf = input("Digite o CPF (formato: xxx.xxx.xxx-xx): ")

# Removendo os caracteres não numéricos do CPF usando o método replace
cpf_numeros = cpf.replace(".", "").replace("-", "")

# Verificando se o CPF tem 11 dígitos
if len(cpf_numeros) != 11:
    print("CPF inválido. Deve conter 11 dígitos.")
else:
    # Convertendo os dígitos do CPF para inteiros
    digitos_cpf = [int(digito) for digito in cpf_numeros]

    # Validando o primeiro dígito verificador (método do exercício anterior)
    multiplicador = 10
    soma = 0
    for i in range(9):
        soma += digitos_cpf[i] * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        primeiro_digito_verificador = 0
    else:
        primeiro_digito_verificador = 11 - resto

    if primeiro_digito_verificador != digitos_cpf[9]:
        print("CPF inválido.")
    else:
        # Validando o segundo dígito verificador
        multiplicador = 11
        soma = 0
        for i in range(10):
            soma += digitos_cpf[i] * multiplicador
            multiplicador -= 1

        resto = soma % 11
        if resto < 2:
            segundo_digito_verificador = 0
        else:
            segundo_digito_verificador = 11 - resto

        if segundo_digito_verificador == digitos_cpf[10]:
            print("CPF válido.")
        else:
            print("CPF inválido.")

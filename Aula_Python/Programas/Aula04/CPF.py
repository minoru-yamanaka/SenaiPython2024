# 3)	Faça um programa que o usuário digite um CPF
# (exemplo: 123.456.789-10) e o sistema valide se o primeiro digito verificador está correto (no caso do exemplo, o número 1 após o traço).
# Para validar este dígito verificador deve seguir os seguintes passo:
# 1.	Multiplicar cada número do CPF por um valor respectivo:
# Ex: CPF 132.465.987-10
#
# 1      3      2      4      6      5      9      8      7
# X
# 10    9      8      7      6      5      4      3      2
# =
# 10   27    16    28    36     25   36    24    14
#
# 2.	Somar os resultados:
#
# 10 + 27 + 16 + 28 + 36 + 25 + 36 + 24 + 14 = 216
#
# 3.	Multiplicar o resultado por 10:
#
# 216 x 10 = 2160
#
# 4.	Obter o resto da divisão do valor por 11:
#
# 2160 % 11 = 4
#
# 5.	Se o resultado anterior for maior que 9 o resultado é 0, se não o resultado anterior é o resultado (no exemplo: 4)
#
# 6.	Se o Resultado for igual ao primeiro dígito verificador está correto, senão está incorreto
# CPF  do exemplo: 132.465.987-10
# 1º Digito verificador: 1
# Resultado do cálculo: 4
# Logo:
# CPF inválido

cpf = input("Digite o CPF (formato: xxx.xxx.xxx-xx): ")

# Removendo os caracteres não numéricos do CPF usando o método replace
cpf_numeros = cpf.replace(".", "").replace("-", "")
#----
# Verificando se o CPF tem 11 dígitos
if len(cpf_numeros) != 11:
    print("CPF inválido. Deve conter 11 dígitos.")
else:
    # Percorrenddo cada num e os convertendo os dígitos do CPF para inteiros
    digitos_cpf = [int(digito) for digito in cpf_numeros]

    # Multiplicando cada dígito do CPF pelo seu respectivo peso
    multiplicador = 10
    soma = 0
    for i in range(9):
        soma += digitos_cpf[i] * multiplicador
        multiplicador -= 1

    # Calculando o dígito verificador
    resto = soma % 11
    if resto < 2:
        primeiro_digito_verificador = 0
    else:
        primeiro_digito_verificador = 11 - resto

    # Validando o primeiro dígito verificador
    if primeiro_digito_verificador == digitos_cpf[9]:
        print("O primeiro dígito verificador é válido.")
    else:
        print("O primeiro dígito verificador é inválido.")



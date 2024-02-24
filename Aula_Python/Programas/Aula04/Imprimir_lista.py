# 1)Para a str a seguir:
# jose
# jorge
# maria
# antonio
# ana
# julia
# márcio
# fernando
# zelia

lista = '''jose 
jorge
maria
antonio
ana
julia
márcio
fernando
zelia
'''

# Faça um programa para imprimir estes dados com os índices de cada um.
# Exemplo:
# 1 – jose
# 2 – jorge
# 3 – maria

# Nomes, imprimindo-os com seus índices
for indice, nome in enumerate(lista, start=1):
    print( str(indice) + '-' + str(nome))
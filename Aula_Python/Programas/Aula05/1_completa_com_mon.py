def completa_com_mon(nome):
    if len(nome) >= 4:
        prefixo = nome[:4]
        return prefixo + 'mon'
    else:
        return "O nome é muito curto para ser completado com 'mon'."

# Exemplo de uso:
nome = str(input("insira seu nome: "))
nome_completo = completa_com_mon(nome)
print(nome_completo)  # Saída: Danimon


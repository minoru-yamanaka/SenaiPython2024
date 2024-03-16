# # criar arq -
# with open("Arquivos/arquivo.txt", "w")as arq:
#     arq.write("Olá mundo !\n")
import time

import mouse

# with open("Arquivos/arquivo.txt", "w")as file:
#     file.write("teste\n")

# with open("Arquivos/arquivo.txt", "r")as file:
#     print(file.read())

# with open ("Arquivos/arquivo.txt", "a")as file:
#     file.write("Nova linha")

# with open ("Arquivos/arquivo.txt", "r")as file:
#     print(file.read())

# ---

# import csv
# lista_de_nomes = ["joão", "daniel", "ana"]
#     csv.writer(file).writerow(lista_de_nomes)
#
# Este código em Python está importando o módulo csv, que é usado para
# trabalhar com arquivos CSV (Comma Separated Values). Em seguida, cria
# uma lista chamada lista_de_nomes com três nomes: "joão", "daniel" e "ana".
#
# Depois, o código abre um arquivo chamado "pessoas.csv" em modo de escrita
# ("w"). Dentro do bloco with, ele utiliza o método writerow() do objeto
# csv.writer(file) para escrever uma linha no arquivo CSV.

# import csv
# with open("Arquivos/pessoas.csv", "r")as file:
#      reader =csv.reader(file)
#      for linha in reader:
#          print(linha)

# # mapear click
# import mouse
#
# while True:
#     if mouse.is_pressed("left"):
#         print(mouse.get_position())
#         time.sleep(0.5)
#     elif mouse.is_pressed("middle"):
#         break





import sys


file = input()

numberOfOperations = int(input())

listOfOperations = [input() for _ in range(numberOfOperations)]


# OPERACOES
# BUCKET C T COL ROW
# NEGATIVE T COL ROW
# CMASK T COL ROW
# SAVE

new_file = []
actual_file = []

with open(f"{file}",'r') as f:

    data = f.read()

    new_file.append(f"{data[0]}")
    new_file.append('# Imagem criada pelo lab13')
    
    # PEGAR INFORMACOES DA IMAGEM

    actual_file_cols,actual_file_rows = data[2].split(' ')
    actual_file_max = data[3]

    
    for i in range(int(actual_file_rows)):

        linha = (data[4 + i])
        


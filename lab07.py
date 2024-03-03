operador = input()
operando1 = input()
operando2 = input()
numLinhas = int(input())

i = 0
stringTotal = ""
listaStrings = []
while i < numLinhas:
    i += 1
    a = input()
    stringTotal += a
    listaStrings.append(a)


tamString = len(stringTotal)

i = 0
indice = [0,0]
#chave = 0
while i < tamString:

    if ('numero' == operando1 and stringTotal[i].isdigit()) or stringTotal[i] == operando1 or ('vogal'==operando1 and stringTotal[i] in ['A','E','I','O','U','a','e','i','o','u']):
        indice[0] = i
        
        #i = i + 1

        while i < tamString:
            if ('numero' == operando2 and stringTotal[i].isdigit()) or stringTotal[i] == operando2 or ('vogal'==operando2 and stringTotal[i] in ['A','E','I','O','U','a','e','i','o','u']):
                indice[1] = i
                break
            i = i + 1



        break

    i = i + 1
#print(indice)
chave = 0
if operador == "+":
    chave = indice[0] + indice[1]
elif operador == '-':
    chave = indice[0] - indice[1]
elif operador == '*':
    chave = indice[0] * indice[1]

print(chave)

for item in listaStrings:
    newString = ""
    for j in range(len(item)):
        asciiValue = ord(item[j]) + chave
        if asciiValue < 32:
            asciiValue = ord(item[j]) -chave - chave - 1
        while asciiValue > 126:
            asciiValue = 31 + (asciiValue - 126)
         
        newString += chr(asciiValue)

    print(newString)
    
numLinhas = int(input())

matriz = []

for i in range(numLinhas):
    linha = input().split()
    matriz.append(linha)

y,x = 0,0

tamLinhas = len(matriz[0])
tamColunas = len(matriz)

passo = 1

def printaMatriz(matriz):
    for i in range(len(matriz)):
        a = ""
        for l in range(len(matriz[0])):
            #print(matriz[i][l],'', end="")
            a += matriz[i][l] + ' '
        print(a.strip())
    print()

while y < tamColunas and x < tamLinhas:
    


    matriz[y][x] = 'r'

    printaMatriz(matriz)

    matriz[y][x] = '.'

    if tamColunas % 2 == 1:
        if y+1 == tamColunas and x+1 == tamLinhas :
            break
    if tamColunas % 2 == 0:
        if y+1 == tamColunas and x == 0:
            
            for i in range(tamLinhas):
                matriz[y][x] = '.'
                x += 1
                matriz[y][x] = 'r'
                printaMatriz(matriz)

            
            break



    x += passo

    if x == tamLinhas:
        passo = -1
        x += passo
        y += 1
    
    elif x == -1:
        passo = 1
        x += passo
        y += 1
    

    matriz[y][x] = 'r'



    ###CHECA A POSICAO INFERIOR
    listaParaVoltar = [(y,x)]
    try:
        if matriz[y+1][x] == 'o':
            ##MODO LIMPEZA

            printaMatriz(matriz)
            matriz[y][x] = '.'
            y += 1
            matriz[y][x] = 'r'

            printaMatriz(matriz)

            matriz[y][x] = '.'

            listaParaVoltar.append((y,x))

            while True:
                
                try:
                        
                    if x-1 >= 0:
                        if matriz[y][x-1] == 'o':
                            x -= 1
                            matriz[y][x] = 'r'
                            printaMatriz(matriz)
                            matriz[y][x] = '.'
                            listaParaVoltar.append((y,x))
                            continue
                    if y - 1 >= 0:
                        if matriz[y-1][x] == 'o':
                            y -= 1
                            matriz[y][x] = 'r'
                            printaMatriz(matriz)
                            matriz[y][x] = '.'
                            listaParaVoltar.append((y,x))
                            continue
                    if x+1 < tamLinhas:
                        if matriz[y][x+1] == 'o':
                            x += 1
                            matriz[y][x] = 'r'
                            printaMatriz(matriz)
                            matriz[y][x] = '.'
                            listaParaVoltar.append((y,x))
                            continue
                    if y + 1 < tamColunas:
                        if matriz[y+1][x] == 'o':
                            y += 1
                            matriz[y][x] = 'r'
                            printaMatriz(matriz)
                            matriz[y][x] = '.'
                            listaParaVoltar.append((y,x))
                            continue
                    
                    break
                except IndexError:
                    break

            
            ##FAZER CAMINHO INVERSO
            listaParaVoltar.pop()
            for i in range(1,len(listaParaVoltar)):
                step = listaParaVoltar.pop()
                y,x = step
                matriz[y][x] = 'r'
                printaMatriz(matriz)
                matriz[y][x] = '.'

            y,x = listaParaVoltar.pop()
            
            
    except IndexError:
        pass

print()
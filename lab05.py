genoma = input("")


def reverter(gen,i,j):
    #print(gen,i,j)
    genToRevert = gen[i:j+1] #trecho a reverter

    initGen = gen[0:i] #inicio fixo
    restGen = gen[j+1:] #final fixo
    
    subGen = ""
    k = 1
    while k <= (len(genToRevert)):
        
        subGen += genToRevert[len(genToRevert)-k]
        k += 1
    return initGen+subGen+restGen


def transpor(gen,i,j,k):
    firstPartGen = gen[0:i]
    secondPartGen = gen[i:j+1]
    thirdPartGen = gen[j+1:k+1]
    forthPartGen = gen[k+1:]

    return firstPartGen + thirdPartGen + secondPartGen + forthPartGen


def combinar(gen, genAdd, i):

    return gen[0:i] + genAdd + gen[i:]

def concatenar(gen, genAdd):
    return gen + genAdd

def remover(gen, i,j):
    return gen[0:i] + gen[j+1:]

def transpor_e_reverter(gen,i,j,k):
    genTemp = transpor(gen,i,j,k)
    return reverter(genTemp,i,k)

def buscar(genoma, gene):

    i = 0
    tam = len(gene)
    counter = 0
    while i < len(genoma):

        if gene == genoma[i:i+tam]:
            i += tam
            counter += 1
        else:
            i += 1
    return counter

def buscar_bidirecional(genoma,gene):

    counter = 0

    counter +=buscar(genoma,gene)
    
    #print(gene,genoma,counter)
    counter += buscar(reverter(genoma,0,len(genoma)),gene)
    #print(gene,reverter(genoma,0,len(genoma)),counter)
    return counter

def mostrar(gen):
    return gen

entrada = ""

while entrada != "sair":

    entrada = input("").split()

    if entrada[0] == "sair":
        break
    
    lista = ["reverter","transpor","combinar","concatenar","remover","transpor_e_reverter","buscar","buscar_bidirecional","mostrar"]

    if entrada[0] not in lista:
        continue
    temp = ""
    if entrada[0] == lista[0]:
        temp = reverter(genoma,int(entrada[1]),int(entrada[2]))
        genoma = temp
    elif entrada[0] == lista[1]:
        temp = transpor(genoma, int(entrada[1]),int(entrada[2]),int(entrada[3]))
        genoma = temp
    elif entrada[0] == lista[2]:
        temp = combinar(genoma,entrada[1],int(entrada[2]))    
        genoma = temp
    elif entrada[0] == lista[3]:
        temp = concatenar(genoma,entrada[1])
        genoma = temp
    elif entrada[0] == lista[4]:
        temp = remover(genoma,int(entrada[1]),int(entrada[2]))
        genoma = temp
    elif entrada[0] == lista[5]:
        temp = transpor_e_reverter(genoma,int(entrada[1]),int(entrada[2]),int(entrada[3]))
        genoma = temp
    elif entrada[0] == lista[6]:
        temp = buscar(genoma,entrada[1])
        print(temp)
        
    elif entrada[0] == lista[7]:
        temp = buscar_bidirecional(genoma,entrada[1])
        print(temp)
        
    elif entrada[0] == lista[8]:
        temp = mostrar(genoma)
        print(temp)
    
    #print(temp)  
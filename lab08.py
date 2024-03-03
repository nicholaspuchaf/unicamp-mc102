numeroDeFilmes = input()

dictionarioFilmes = {}

for _ in range(int(numeroDeFilmes)):
    filme = input()
    dictionarioFilmes[filme] = {'filme que causou mais bocejos':[0,0],'filme que foi mais pausado':[0,0], 'filme que mais revirou olhos':[0,0],'filme que não gerou discussão nas redes sociais':[0,0], 'enredo mais sem noção':[0,0]} #filme que causou mais bocejos, filme que foi mais pausado, filme que mais revirou olhos, filme que não gerou discussão nas redes sociais e enredo mais sem noção;

numeroDeAvaliacoes = int(input())
i = 0
while i < numeroDeAvaliacoes:
    i = i + 1

    argumentos = input().split(',') # avaliador 2, filme que causou mais bocejos, ninguém é de ninguém, 10
    
    nomeDoFilme = argumentos[2].strip()
    criterio = argumentos[1].strip()
    nota = int(argumentos[3].strip())

    dictionarioFilmes[nomeDoFilme][criterio] = [dictionarioFilmes[nomeDoFilme][criterio][0] + nota,dictionarioFilmes[nomeDoFilme][criterio][1] + 1]

#CALCULAR AS MEDIAS

dicionarioMaioresMedias = {'filme que causou mais bocejos':[0,0],'filme que foi mais pausado':[0,0], 'filme que mais revirou olhos':[0,0],'filme que não gerou discussão nas redes sociais':[0,0], 'enredo mais sem noção':[0,0]}

listaNaoDeviaEstarAqui = []

for nomeFilme, dados in dictionarioFilmes.items():
    #dados é um dicionario tbm

    flagNaoDeviaEstarAqui = True

    #print(nomeFilme, dados)

    for categoria, subLista in dados.items():

        if subLista[1] != 0: #numero de votantes
            subLista = [float(subLista[0])/float(subLista[1]),subLista[1]]
            flagNaoDeviaEstarAqui = False

        if dicionarioMaioresMedias[categoria][1] < subLista[0]:
            dicionarioMaioresMedias[categoria] = [nomeFilme,subLista[0]]

        if dicionarioMaioresMedias[categoria][1] == subLista[0] and dicionarioMaioresMedias[categoria][0] != 0:

            nomeTemp = dicionarioMaioresMedias[categoria][0]
            votosTemp = dictionarioFilmes[nomeTemp][categoria][1]

            if votosTemp < subLista[1]:
                dicionarioMaioresMedias[categoria] = [nomeFilme, subLista[0]]
            
            #dicionarioMaioresMedias[categoria] = 

        # if dicionarioMaioresMedias[categoria][1] == subLista[0]:
        #     if dicionarioMaioresMed
        

    if flagNaoDeviaEstarAqui == True:
        listaNaoDeviaEstarAqui.append(nomeFilme)


#CAlCULA PIOR FILME DE TODOS
pior = ['',0,0]
dicioPerdedorMaximo = {}


for criterio, nomeFilmeEDado in dicionarioMaioresMedias.items():
    
    # media = 0
    # for value in dictionarioFilmes[nomeFilmeEDado[0]].values():
    #     media = media + value[0]

    #print(criterio,nomeFilmeEDado)

    if dicioPerdedorMaximo.get(nomeFilmeEDado[0]):
        dicioPerdedorMaximo[nomeFilmeEDado[0]][0] += 1
        dicioPerdedorMaximo[nomeFilmeEDado[0]][1] += nomeFilmeEDado[1] 

    else:
        dicioPerdedorMaximo[nomeFilmeEDado[0]] = [1,nomeFilmeEDado[1]]

    if pior[1] < dicioPerdedorMaximo[nomeFilmeEDado[0]][0]:
        pior = [nomeFilmeEDado[0], dicioPerdedorMaximo[nomeFilmeEDado[0]][0], dicioPerdedorMaximo[nomeFilmeEDado[0]][1]]
    if pior[1] == dicioPerdedorMaximo[nomeFilmeEDado[0]][0]:
        if pior[2] < dicioPerdedorMaximo[nomeFilmeEDado[0]][1]:
            pior = [nomeFilmeEDado[0], dicioPerdedorMaximo[nomeFilmeEDado[0]][0], dicioPerdedorMaximo[nomeFilmeEDado[0]][1]]

    #print(pior, nomeFilmeEDado[0],dicioPerdedorMaximo[nomeFilmeEDado[0]])
    
print("#### abacaxi de ouro ####")
print()

print("categorias simples")
print("categoria: filme que causou mais bocejos")
print("-", dicionarioMaioresMedias['filme que causou mais bocejos'][0])

print("categoria: filme que foi mais pausado")
print("-", dicionarioMaioresMedias['filme que foi mais pausado'][0])

print("categoria: filme que mais revirou olhos")
print("-", dicionarioMaioresMedias['filme que mais revirou olhos'][0])

print("categoria: filme que não gerou discussão nas redes sociais")
print("-", dicionarioMaioresMedias['filme que não gerou discussão nas redes sociais'][0])

print("categoria: enredo mais sem noção")
print("-", dicionarioMaioresMedias['enredo mais sem noção'][0])

print()

print("categorias especiais")
print("prêmio pior filme do ano")
print('-', pior[0])
print("prêmio não merecia estar aqui")
if not listaNaoDeviaEstarAqui:
    print('- sem ganhadores')
if len(listaNaoDeviaEstarAqui) == 1:
    print('-', listaNaoDeviaEstarAqui[0])
if len(listaNaoDeviaEstarAqui) > 1:
    string = listaNaoDeviaEstarAqui[0]
    for i in range(1,len(listaNaoDeviaEstarAqui)):
        string = string + ', ' + listaNaoDeviaEstarAqui[i]
        
    print('-', string)

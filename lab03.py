numJogadores = int(input())

numeRetirados = input().split()

for i in range(len(numeRetirados)):
    numeRetirados[i] = int(numeRetirados[i])

numeIntervalos = input().split()

for i in range(len(numeIntervalos)):
    numeIntervalos[i] = int(numeIntervalos[i])

i = 0
# numMax = [-1,-99999]
# numMin = [-1,999999]

pontuacoes = []

while i < numJogadores:
    if (i < numJogadores//2 and numJogadores%2 ==0) or (i<=numJogadores//2 and numJogadores%2==1):#par
        ponto = ((numeIntervalos[i*2] - numeIntervalos[2*i+1]) * -1) * numeRetirados[i]
        # numMax = [i,ponto] if ponto > numMax[1] else numMax
        # numMin = [i,ponto] if ponto < numMin[1] else numMin
    else: #(i < numJogadores//2 and numJogadores%2 ==0) or (i<=numJogadores//2 and numJogadores%2==1):#par
        ponto = ((numeIntervalos[i*2] - numeIntervalos[2*i+1]) * -1) + numeRetirados[i]
        # numMax = [i,ponto] if ponto > numMax[1] else numMax
        # numMin = [i,ponto] if ponto < numMin[1] else numMin
    pontuacoes.append(ponto)
    i +=1 

numMax = [pontuacoes[0],1]
num2Max = [pontuacoes[0] - 10,False]

for i in range(1,len(pontuacoes)):
    if pontuacoes[i] > numMax[0]:
        numMax = [pontuacoes[i],i+1]
    elif pontuacoes[i] > num2Max[0]:
        num2Max = [pontuacoes[i], i+1]

if num2Max[0] == numMax[0]:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print("O jogador número", numMax[1], "vai receber o melhor bolo da cidade pois venceu com", numMax[0],"ponto(s)!")


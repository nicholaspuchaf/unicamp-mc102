numDias = int(input())
it = 0

while it < numDias:
	it += 1
	numAnimais = int(input())
	nomeAnimais = []
	i = 0
	while i < numAnimais:
		i = i + 1
		nomeAnimais.append(input().split())

	#print(nomeAnimais)

	mapa = {}

	proceds = input().split()

	i = 0
	while i < len(proceds):
		mapa[proceds[i]] = int(proceds[i+1])	
		i = i + 2
	#print(mapa)
	numAtendimentos = int(input())

	jaAtendidos = []

	naoAtendidos = []

	semProcedimentos = []

	animaisBrigados = 0

	jaPassaram = []

	i = 0
	while i < numAtendimentos:
		i = i + 1

		par = input().split()

		for k in nomeAnimais:
			if par[0] in k:
				for l in jaPassaram:
					if l in k:
						animaisBrigados += 1

		jaPassaram.append(par[0])

		if mapa.get(par[1]):
			if mapa[par[1]] > 0:
				jaAtendidos.append(par[0])
				mapa[par[1]] = mapa[par[1]] - 1
			if mapa[par[1]] < 0:
				naoAtendidos.append(par[0])
			if mapa[par[1]] == 0:
				mapa[par[1]] = mapa[par[1]] - 1
		else:
			semProcedimentos.append([par[0],par[1]])

		"""if not mapa.get(par[1]):
			semProcedimentos.append([par[0],par[1]])
			continue
		elif mapa[par[1]] > 0:
			jaAtendidos.append(par[0])
			mapa[par[1]] = mapa[par[1]] - 1
		else:
			naoAtendidos.append(par[0])
			continue"""

	if it > 1:
		print()	
	print("Dia:", it)
	print("Brigas:",animaisBrigados)

	nomes = ""
	
	if jaAtendidos:
		for il in jaAtendidos:
			nomes = nomes + il +", "

		print("Animais atendidos:", nomes[:len(nomes)-2])
	nomesN = ""
	#print(naoAtendidos)
	if naoAtendidos:
		for il in naoAtendidos:
			nomesN = nomesN + il + ", "
		nomesN = nomesN[:len(nomesN)-2]
		print("Animais não atendidos:",nomesN)
	tamSemProcedimentos = len(semProcedimentos)
	il = 0
	while il < tamSemProcedimentos:
		print("Animal", semProcedimentos[il][0],"solicitou procedimento não disponível.")
		il = il + 1


def fibo(n):
	inicial = [1,1]

	for i in range(n-2):
		inicial.append(inicial[-1]+inicial[-2])

	return inicial[-1]


variavel = int(input(""))
res = fibo(variavel)

print("O termo na posição {0} da sequência de Fibonacci é: {1}.".format(variavel,res))
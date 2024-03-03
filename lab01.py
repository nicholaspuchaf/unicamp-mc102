var1 = input("")
var2 = input("")


if var1 == "tesoura":
	if var2 in ["spock","pedra"]:
		print("Jornada nas Estrelas")
		
	elif var2 == "tesoura":
		print("empate")
	else:
		print("Interestelar")
elif var1 == "pedra":
	if var2 == "pedra":
		print("empate")
	elif var2 in ["spock","papel"]:
		print("Jornada nas Estrelas")
	else:
		print("Interestelar")
elif var1 == "lagarto":
	if var2 == "lagarto":
		print("empate")
	elif var2 in ["pedra","tesoura"]:
		print("Jornada nas Estrelas")
	else:
		print("Interestelar")
elif var1 == "papel":
	if var2 == "papel":
		print("empate")
	elif var2 in ["tesoura","lagarto"]:
		print("Jornada nas Estrelas")
	else:
		print("Interestelar")
elif var1 == "spock":
	if var2 == "spock":
		print("empate")
	elif var2 in ["papel","lagarto"]:
		print("Jornada nas Estrelas")
	else:
		print("Interestelar")

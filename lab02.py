



print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")

print("Seu SO anterior era Linux?")
print("(0) Não")
print("(1) Sim")

a = input()

if a == "0":

    print("Seu SO anterior era um MacOS?")  

    print("(0) Não")
    print("(1) Sim")

    b = input()

    if b == "0":
        
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.")
        exit(0)
    if b == "1":
        
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.")
        exit(0)
    else:
        print("Opção inválida, recomece o questionário.")
        exit(0)
        

if a == "1":

    print("É programador/ desenvolvedor ou de áreas semelhantes?")

    print("(0) Não")
    print("(1) Sim")
    print("(2) Sim, realizo testes e invasão de sistemas")

    b = input() 

    if b == "0":

        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.")
        exit(0)
    if b == "2":
        
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.")
        exit(0)
        

    if b == "1":

        print("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?")
        print("(0) Não")
        print("(1) Sim")

        c = input()

        if c == "0":

            print("Já utilizou Arch Linux?")
            print("(0) Não")
            print("(1) Sim")

            d = input()

            if d == "0":

                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.")
                exit(0)

            if d == "1":

                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.")
                exit(0)
                
            else:
                print("Opção inválida, recomece o questionário.")
                exit(0)

        if c == "1":

            print("Já utilizou Debian ou Ubuntu?")
            print("(0) Não")
            print("(1) Sim")

            d = input()

            if d == "0":

                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.")
                exit(0)

            if d == "1":

                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.")
                exit(0)

            else:
                print("Opção inválida, recomece o questionário.")
                exit(0)


        else:
            print("Opção inválida, recomece o questionário.")
            exit(0)

    else:
        print("Opção inválida, recomece o questionário.")
        exit(0)


else:
    print("Opção inválida, recomece o questionário.")
    exit(0)
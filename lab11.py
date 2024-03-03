class Mapa():

    def __init__(self, personagem, tamLinhas : int = 0, tamColunas : int = 0, posInicial : tuple = (0,0), posFinal : tuple = (0,0), numero_monstros : int = 0):
        self.tamLinhas = tamLinhas
        self.tamColunas = tamColunas

        self.posicaoInicial : tuple = posInicial
        self.posicaoSaida : tuple = posFinal

        self.numero_monstros = numero_monstros

        self.matriz = []

        self.listaDosMonstros = []

        self.listaDosObjetos = []

        self.personagem = personagem



    def desce_link_ate_o_final(self):
        pass
    

    def verifica_encontro(self):
        pass

    def pega_dados(self):
        temp = input().split()
        self.tamLinhas = int(temp[0])
        self.tamColunas = int(temp[1])
        temp = input()
        self.posicaoInicial = (int(temp[0]), int(temp[2]))
        temp = input()
        self.posicaoSaida = (int(temp[0]), int(temp[2]))
        temp = input()
        self.numero_monstros = int(temp)

    def cria_matriz(self):

        self.pega_dados()

        for i in range(self.tamColunas):
            self.matriz.append([])
            for j in range(self.tamLinhas):
                self.matriz[i].append('.')    


        self.matriz[self.posicaoInicial[0]][self.posicaoInicial[1]] = 'P'
        self.matriz[self.posicaoSaida[0]][self.posicaoSaida[1]] = '*'
        
        self.adiciona_monstros_na_matriz()
        self.adiciona_objetos()

    def mostra_matriz(self):

        for i in range(self.tamLinhas):
            print()
            for j in range(self.tamColunas):
                print(self.matriz[i][j], end=' ')

    def adiciona_monstros_na_matriz(self):          

        for num in range(self.numero_monstros):

            linha = input().split()

            vida = int(linha[0])
            ataque = int(linha[1])
            tipo = linha[2]
            posInicial = (int(linha[3][0]), int(linha[3][2]))

            monstro = Monstro(vida,ataque, tipo, posInicial)

            self.matriz[posInicial[0]][posInicial[1]] = tipo
            
            self.listaDosMonstros.append(monstro)

    def adiciona_objetos(self):
        numeroDeObjetos = int(input())

        for _ in range(numeroDeObjetos):
            tempData = input().split(' ')
            nome = tempData[0]    
            tipo = tempData[1]
            valor = tempData[3]
            posicao = (int(tempData[2][0]),int(tempData[2][2]))

            objeto = Objeto(nome,tipo,posicao,valor)

            self.listaDosObjetos.append(objeto)

            self.matriz[posicao[0]][posicao[1]] = objeto.tipo



class Objeto():

    def __init__(self, nome,tipo, posicao, valor):
        self.nome = nome
        self.tipo = tipo
        self.posicao = posicao
        self.valor = valor

class Entidade():
    
    def __init__(self, vida : int, ataque : int,):
        self.vida = vida
        self.ataque = ataque

class Monstro(Entidade):

    def __init__(self, vida : int, ataque : int, tipo : str, posInicial : tuple):
        super().__init__(vida,ataque)
        self.tipo = tipo
        self.posInicial = posInicial
        
class Link(Entidade):
    
    def __init__(self, vida : int, ataque : int):
        super().__init__(vida,ataque)




if __name__ == "__main__":

    temp = input().split()

    link = Link(int(temp[0]), int(temp[1]))

    mapa = Mapa()
    mapa.cria_matriz()
    mapa.mostra_matriz()
    
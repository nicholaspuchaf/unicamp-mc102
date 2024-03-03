
class Chao():

    def __init__(self, num):

        self.numLinhas = num

        self.matriz = self.cria_matriz()

    def cria_matriz(self):
        matriz = []
        for i in range(self.numMatriz):
            
            linha = input().split(" ")
            
            matriz.append(linha)

        return matriz
            


    def imprime_matriz(self, posRobo):

        for i in range(len(self.matriz)):
            string = ''
            for j in range(len(self.matriz[0])):
                
                if i == posRobo[0] and j == posRobo[1]:
                    #print('r ')
                    string += 'r '

                #print(self.matriz[i][j], end=' ')
                string += self.matriz[i][j] + ' '
            
            print(string.strip()) 


class Robo():


    def __init__(self, chao):

        self.x = 0
        self.y = 0
        self.direcao = 'dir'
        self.chao = chao
        self.modo = "scan"
        self.ultimaPosAntesLimpeza = [0,0]


    def escaneamento(self):
        
        # VERIFICAR NAS ADJACENCIAS
        if self.verifica_baixos():
            # Há sujeira em baixo

            self.modo = 'limpeza'
            self.ultimaPosAntesLimpeza = [self.y, self.x]
            self.limpeza(self.y+1,self.x)
            


        # SE NAO ENCONTRAR MOVER-SE PARA O PROXIMA POSICAO
        else:
            # movimentarse 
            self.movimentar()
            
    def movimentar(self):

        if self.direcao == 'dir':
            self.x += 1

            if len(self.chao.matriz[0]) == self.x:
                # CHEGOU NA PAREDE
                self.y += 1
                self.x -= 1
                self.direcao = 'esq'

        
        elif self.direcao == 'esq':
            self.x -= 1

            if len(self.chao.matriz[0]) == 0:
                # CHEGOU NA PAREDE
                self.y += 1
                self.x += 1
                self.direcao = 'dir'

        if len(self.chao.matriz) == self.y:
            # CHEGOU ATÈ O FINAL
            pass

    def verifica_baixos(self):

        if self.chao.matriz[self.y+1][self.x]:
            # Há sujeira em baixo
            return True
        else:
            return False

    def limpeza(self, posY, posX):
        
        self.y = posY
        self.x = posX

        self.chao.matriz[self.y][self.x] = '.'

        # VERIFICAR SE HA SUJEIRA NAS ADJACENCIAS

        verificacao = self.verifica_ao_redor()

        if verificacao == False:

            self.modo = 'retornar'

            return False, False
        else:
            
            return verificacao[0], verificacao[1]

        # SE NAO MODO RETORNAR

    def verifica_ao_redor(self):

        if self.x-1 >= 0:
            if self.chao.matriz[self.y][self.x-1] == 'o':

                # TEM SUJEIRA
                return [self.y,self.x-1]

        if self.y-1 >= 0:

            if self.chao.matriz[self.y-1][self.x] == 'o':

                # TEM SUJEIRA
                return [self.y-1, self.x]

        if self.x+1 < len(self.chao.matriz[0]): 

            if self.chao.matriz[self.y][self.x+1] == 'o':

                # TEM SUJEIRA
                return [self.y, self.x+1]
        if self.y+1 < len(self.chao.matriz):

            if self.chao.matriz[self.y+1][self.x] == 'o':
                
                # TEM SUJEIRA

                return [self.y+1, self.x]

        return False


if __name__ == "__main__":

    chao = Chao(input())

    robo = Robo(chao)
    posY, posX = 0,0
    while 1:

        if robo.modo == 'scan':
            
            robo.escaneamento()

        elif robo.modo == 'limpeza':

            posY,posX = robo.limpeza()

        elif robo.modo == 'retornar':
            
            robo.retornar()
        
        elif robo.modo == 'finalizar':

            robo.finalizar()

        
        chao.imprime_matriz(robo.y,robo.x)
import math

class Aloy():

    def __init__(self, max_hp : float, arrows_input : str, nMachines : int):
        self.max_hp :float = float(max_hp)
        self.max_hp_default : float = float(max_hp)
        self.arrows_input = arrows_input
        self.aloy_arrows = self.parse_aloy_arrows(self.arrows_input)
        self.aloy_arrows_backup = dict(self.aloy_arrows)

        self.critical_hits_of_round = {}


        self.machinesToBeatTotal = nMachines
        self.machineCounter = 0
        self.combatCounter = 0

        self.numMachinesSimul = 0

        self.listAllMachinesBackup = []
        self.listAllAloyAttacksBackup = []
        self.string_return_final = []

        self.machines_killed_round = []

    def parse_aloy_arrows(self, arrowsInput : str) -> dict: 

        #arrows = input().split("")
        arrows = arrowsInput.split(" ")
        dicto = {}

        for i in range(0,len(arrows),2):
            dicto[arrows[i]] = int(arrows[i+1])

        return dicto

    def start(self):
        '''Inicia o combate da Aloy, e calcula quantos combates serao necessários'''

        self.numMachinesSimul = int(input())

        i = 0
        numOfCombats = self.machinesToBeatTotal
        while i < numOfCombats:
            
            if i > 0:
                self.numMachinesSimul = int(input())

            fast_checker = self.start_single_combat(self.numMachinesSimul)

            if fast_checker == "Aloy is dead":
                return False
            if fast_checker == "Aloy got no arrows":
                return False

            i += self.numMachinesSimul
        # numRest = self.machinesToBeatTotal%self.numMachinesSimul

        # if numRest:
        #     self.start_single_combat(numRest)


        ## COMO NAO MORREU E ESTA SAFE PODE TERMINAR

        self.string_return_final.append(f"Aloy provou seu valor e voltou para sua tribo.")

    def start_single_combat(self, numEnemies : int):
        '''Roda apenas um combate com os U inimigos simultaneos do combate'''

        # print("Combate", self.combatCounter, "vida =", self.max_hp)
        self.string_return_final.append(f"Combate {self.combatCounter}, vida = {int(self.max_hp)}")

        self.combatCounter += 1

        listMachinesOfRound = []

        self.critical_hits_of_round = {}


        self.machineCounter = 0

        for _ in range(numEnemies):
            """ Foi Criada uma lista com todas as maquinas a serem combatidas"""
            machine = Machine(self.machineCounter,input()) ### BIXO È CRIADO
            machine.machinePartsParsed = machine.parse_machine_parts(machine.listMachineParts, self.critical_hits_of_round)
            self.machineCounter += 1

            listMachinesOfRound.append(machine)
            self.listAllMachinesBackup.append(machine)

        self.machines_killed_round = []

        flag_to_machine_attack = 0
        
        while self.check_if_continues_round(listMachinesOfRound):
            """Irá rodar while enquanto estiver ocorrendo ataques"""

            flag_to_machine_attack += 1
            aloy_attack = self.get_aloy_attack()
            self.listAllAloyAttacksBackup.append(aloy_attack)
            
            self.run_aloy_attack(aloy_attack, listMachinesOfRound)

            if flag_to_machine_attack == 3:
                flag_to_machine_attack = 0
                # ALOY RECEBE DANO

                self.aloy_recieve_damage(listMachinesOfRound)

            
            ## CHECAR SE ALGUMA MAQUINA MORREU SE MORREU DEVE SER ADICIONADA
            
            self.check_death_pre_machine(listMachinesOfRound)
        

        ## CHECAR SE A ALOY MORREU

        if self.check_aloy_is_dead():
            return "Aloy is dead"
        

        

        ## CHECAR SE AS FLECHAS ACABARAM

        got_no_arrows_checker = self.check_aloy_got_arrows()

        if got_no_arrows_checker == "Aloy got no arrows":
            return "Aloy got no arrows"

        ## CHECAR QUAIS ROBOS MORRERAM 

        # got_machines = self.check_all_machine_dead(listMachinesOfRound) DEPRECATED

        self.add_dead_machines()

        self.string_return_final.append(f"Vida após o combate = {int(self.max_hp)}")
        
        ## RECUPERACAO DE VIDA POS COMBATE


        if self.max_hp > 0:
            self.aloy_hp_recover()


        ## MOSTRA QUAIS FLECHAS FORAM UTILIZADAS 

        self.which_arrows_used()


        ## MOSTRA QUAIS CRITICOS FORAM ACERTADOS


        self.check_critical_hitted()


        ## REALIZAR PRINT DAS INFORMACOES APOS FINALIZAR O COMBATE

        # self.string_return_final.append(f"Aloy provou seu valor e voltou para sua tribo.")
        

        # print(self.string_return_final)
     
    def aloy_recieve_damage(self, machines_round):

        for machine in machines_round:

            if machine.machineHP > 0:
                
                self.max_hp -= machine.machineAttackPoints

    def check_death_pre_machine(self, round_machines):
        for machine in round_machines:
            
            item = machine.machineNum

            if item in self.machines_killed_round:
                ## DOES NOTHING
                pass

            elif machine.machineHP <= 0 :
                self.machines_killed_round.append(item)

    def add_dead_machines(self):
        for item in self.machines_killed_round:
            self.string_return_final.append(f"Máquina {item} derrotada")

    def check_aloy_is_dead(self):
        """ Retorna positivo se a Aloy morreu """
        if self.max_hp <= 0:
            # Mureu
            self.add_dead_machines()
            self.string_return_final.append(f"Vida após o combate = 0")
            self.string_return_final.append(f"Aloy foi derrotada em combate e não retornará a tribo.")
            return True
        return False

    def check_aloy_got_arrows(self):
        got_no_arrows = self.calc_all_arrows()

        if got_no_arrows:
            
            self.string_return_final.append(f"Vida após o combate = {int(self.max_hp)}")

            self.string_return_final.append(f"Aloy ficou sem flechas e recomeçará sua missão mais preparada.")


            return "Aloy got no arrows"
        
        return True

    def check_all_machine_dead(self, listMachinesOfRound):
        
        for machine in listMachinesOfRound:
            
            if machine.machineHP > 0:
                raise "Error saiu do loop com maquinas vivas"
            else:
                self.string_return_final.append(f"Máquina {machine.machineNum} derrotada")



        return True
        
    def aloy_hp_recover(self):
        newHP = (self.max_hp) + (self.max_hp_default*0.5)

        if newHP > self.max_hp_default:
            self.max_hp = self.max_hp_default
        else:
            self.max_hp = newHP

    def which_arrows_used(self):

        list_arrows_used = {}

        for aType, quant in self.aloy_arrows.items():
            
            arrowQuant = self.aloy_arrows_backup[aType] - quant

            list_arrows_used[aType] = arrowQuant

        self.aloy_arrows = dict(self.aloy_arrows_backup) # ALOY RECOLHE AS FLECHAS QUE UTILIZOU EM COMBATE

        if list_arrows_used:
            self.string_return_final.append("Flechas utilizadas:")

        for aType, quant in list_arrows_used.items():

            if quant > 0: 
                self.string_return_final.append(f"- {aType}: {quant}/{self.aloy_arrows[aType]}")
        
    def check_critical_hitted(self):
        
        if self.critical_hits_of_round:

            superChecker = 0

            self.string_return_final.append(f"Críticos acertados:")

            

            #for machine, critData in self.critical_hits_of_round.items():
            for machineNumber in sorted(self.critical_hits_of_round.keys()):

                critData = self.critical_hits_of_round[machineNumber]

                self.string_return_final.append(f"Máquina {machineNumber}:")

                fragChecker = 0

                for criticals in critData:
                    
                    if criticals[1] > 0:
                        fragChecker = 1
                        superChecker = 1
                        self.string_return_final.append(f"- ({criticals[0][0]}, {criticals[0][1]}): {criticals[1]}x")

                if fragChecker == 0:
                    self.string_return_final.pop()

            if superChecker == 0:
                self.string_return_final.pop()

    def check_if_continues_round(self, listMachines):
        '''Irá checar se continua a rodar os ataques de Aloy, ela deve parar se todos os inimigos do combate morrerem, acabarem as flechas ou ela morrer'''
        
        if self.max_hp <= 0:
            return False
        if self.calc_all_arrows():
            return False
        if self.calc_machines_dead(listMachines):
            return False
        
        return True
        
    def calc_all_arrows(self):
        """Return positivo se acabaram as flechas """
        all_arrows = 0
        for item in self.aloy_arrows.values():
            all_arrows += item
        
        if all_arrows==0:
            return True

    def calc_machines_dead(self, listMachinesOfRound):
        """Retona positivo se todos estiverem mortos"""
        
        for one_machine in listMachinesOfRound:
            if one_machine.machineHP > 0:
                return False
        
        return True

    def run_aloy_attack(self, aloy_attack:dict, listMachinesOfRound:list):
        '''Rodara os ataques de Aloy conforme os dados previstos'''
        
        getMachine = None

        """LOCALIZA QUAL MAQUINA SERA ATACADA"""
        for item in listMachinesOfRound:
            if item.machineNum == aloy_attack['machineNumber']:
                getMachine = item
        """Irá atacar efetivamente a maquina"""

        if getMachine:

            machinePart = aloy_attack['machinePart']
            arrowType = aloy_attack['arrowType']
            attackCords = aloy_attack['attackCords']
            
            if getMachine.machinePartsParsed[machinePart]['weakness'] == arrowType:
                # DOUBLE DAMAGE

                #self.aloy_arrows[arrowType] -= 1

                damage = self.damage_calc(1,getMachine,attackCords,machinePart)
                getMachine.machineHP -= damage

            elif getMachine.machinePartsParsed[machinePart]['weakness'] == "nenhuma":
                # SIMPLE DAMAGE
 
                #self.calc_which_arrow_use()

                damage = self.damage_calc(0.5,getMachine,attackCords,machinePart)
                getMachine.machineHP -= damage

            elif getMachine.machinePartsParsed[machinePart]['weakness'] == "todas" :
                # Double DAMAGE

                #self.calc_which_arrow_use()

                damage = self.damage_calc(1,getMachine,attackCords,machinePart)
                getMachine.machineHP -= damage

            else:
                # SIMPLE DAMAGE

                #self.calc_which_arrow_use()

                damage = self.damage_calc(0.5,getMachine,attackCords,machinePart)
                getMachine.machineHP -= damage
            
            self.aloy_arrows[arrowType] -= 1


            ## ADICIONA O CRITICAL HIT PARA SER MOSTRADO DEPOIS
            if self.calc_critical_hit(machine_cords=getMachine.machinePartsParsed[machinePart]['critical_hit'], aloy_cords= attackCords):

                item_critical_hit = [attackCords, 1]
                
                flag_check_exist = 0
                
                for key, value in self.critical_hits_of_round.items():

                    if key == getMachine.machineNum:

                        for indx in range(len(value)):

                            cords = value[indx][0]

                            if cords == attackCords:
                                self.critical_hits_of_round[key][indx][1] += 1


                # for key, value in self.critical_hits_of_round.items():
                #     if key == getMachine.machineNum:
                #         flag_check = 0
                #         flag_check_exist = 1
                #         for indx in range(len(value)):
                #             cords = value[indx][0]
                #             if cords == attackCords:
                #                 #times += 1

                #                 self.critical_hits_of_round[key][indx][1] += 1
                #                 flag_check = 1
                #         if flag_check == 0:
                #             self.critical_hits_of_round[key].append(item_critical_hit)
                    
                #     # if flag_check_exist == 0:
                #     #     self.critical_hits_of_round[getMachine.machineNum] = [item_critical_hit]
                #     #     flag_check_exist = 1

                # if flag_check_exist == 0:
                #     self.critical_hits_of_round[getMachine.machineNum] = [item_critical_hit]
                #     flag_check_exist = 1
                

        else:
            """ Não foi encontrada a maquina para atacar """
            pass

    def damage_calc(self, increment :int, machine ,cords:tuple, machinePart:str):
        machineCords = machine.machinePartsParsed[machinePart]['critical_hit']
        machineDamage = machine.machinePartsParsed[machinePart]['max_damage']

        damage = increment * (  machineDamage - (abs(machineCords[0] - cords[0]) + abs(machineCords[1] - cords[1])) )
        
        if damage < 0:
            return 0

        return damage

    def calc_critical_hit(self, machine_cords, aloy_cords):
        
        if machine_cords == aloy_cords:
            return True    
        return False

    def get_aloy_attack(self)-> dict:
        '''Pega os dados do ataque da Aloy'''
        dicto = {}
        attack = input().split(", ")

        dicto['machineNumber'] = int(attack[0])
        dicto['machinePart'] = attack[1]
        dicto['arrowType'] = attack[2]
        dicto['attackCords'] = (int(attack[3]), int(attack[4]))
    
        return dicto

    def calc_which_arrow_use(self):
        """ Não utilizado mais"""
        """ Decide qual flecha irá utilizar, a normal ou a que tem em maior quantidade com a Aloy """
        if self.aloy_arrows['normal'] > 0:
                    self.aloy_arrows['normal'] -= 1
        else:
            most_arrows = [0,0]
            for key, value in self.aloy_arrows.items():
                if value > most_arrows[1]:
                    most_arrows = [key,value]
            
            self.aloy_arrows[key] -= 1

    def print_the_result(self):

        for line in self.string_return_final:
            print(line)



class Machine():

    def __init__(self, machineNum : int, machineInputData : str):
        self.machineNum = machineNum

        self.parsedMachineData = self.parse_machine_data(machineInputData)
        self.machineHP = self.parsedMachineData[0]
        self.machineAttackPoints = self.parsedMachineData[1]
        self.machineNumParts = self.parsedMachineData[2]

        self.listMachineParts = self.get_machine_parts()

        # self.machinePartsParsed = self.parse_machine_parts(self.listMachineParts)
        self.machinePartsParsed = {}


    def parse_machine_data(self, inputData : str) -> list:
        data = [int(x) for x in inputData.split(" ")]
        return data
    

    def get_machine_parts(self) -> list:
        listToReturn = []
        for i in range(self.machineNumParts):
            a = input().split(", ")
            listToReturn.append(a)
        return listToReturn 


    def parse_machine_parts(self, listMachineParts : list, dictoDeCriticosDoRound : dict) -> dict:
        dicto = {}

        dictoDeCriticosDoRound[self.machineNum] = []


        for line in listMachineParts:
            
            dicto[line[0]] = {'weakness' : line[1], 'max_damage':int(line[2]), 'critical_hit' : (int(line[3]), int(line[4]))}

            dictoDeCriticosDoRound[self.machineNum].append([dicto[line[0]]['critical_hit'],0])
        return dicto
        

if __name__ == "__main__":

    aloy = Aloy(int(input()), input(), int(input())) #, int(input()))
    
    aloy.start()

    aloy.print_the_result()
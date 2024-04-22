import unittest
from datetime import datetime

class User():
    def __init__(self,name) -> None:
        pass
    

class Voo():
    
    assentos = {
        'A1': None,
        'A2': None,
        'B1': None,
        'B2': None,
    }

    def __init__(self,origin,destiny,horario,price) -> None:
        self.origin = origin
        self.destiny = destiny
        self.horario =horario
        self.price = price
        pass

    def showDatails(self):
        print(f"{self.origin} , {self.destiny}, {self.horario}, {self.price}")

    def checkVoo():
        pass

    def adicionarPassageiro():
        pass


class System():
    availablesFlights = {'BEL':
                            [Voo('BEL','SP',datetime.now,'1200'),
                            Voo('BEL','RJ',datetime.now,'1500')],
                         'SP':
                            [Voo('SP','BH',datetime.now,'1200'),
                             Voo('SP','MTG',datetime.now,'1500')],
                         }
    
    def findFlightsFromAtoB(self,origin,destiny):
        try:
            isso = self.availablesFlights.get(origin)
            voos = []
            for voo in isso:
                if voo.destiny == destiny:
                    voos.append(voo)
            if len(voos) == 0:
                print("Não há voos com o seu destino")
                return []
            return voos
        except TypeError:
            print(f'Não existe voo com a origem em: {origin}')
            return []



    def showFlitghts(self,origin,destiny):
        voos = self.findFlightsFromAtoB(origin,destiny)
        if len(voos) > 0:
            for voo in voos:
                voo.showDatails()

    def selectFlight():
        pass

    def flightDescription():
        pass

    def selectSeats():
        pass

    def checkReservation():
        pass

    def sendEmail():
        pass

    def run(self):  
        print(f"Bem vindo ao sistema de viagens \n\n")
        while True:
            origin = input("Coloque a sigla da cidade você deseja sair. Exemplo(BEL -> Belém): ")
            destiny = input("Coloque a sigla da cidade você deseja sair. Exemplo(BEL -> Belém): ")
            self.showFlitghts(origin,destiny)


if __name__ == '__main__':
    sys = System()

    sys.run()
            
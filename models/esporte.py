from esporte_players import EsportesPlayers

class ModalidadeEsporte:
    def __init__(self, esporte, nome, max_players, min_players, qtd_times):
        self.nome = nome
        self.esporte = esporte
        self.maxPlayers = max_players
        self.minPlayers = min_players
        self.timesQtd = qtd_times

    def getByEsporte(self, esporte):
        print("Não implementado 'getByEsporte' de ModalidadeEsporte")
        pass


class Esporte:
    def __init__(self, nome, icon):
        self.nome = nome
        self.icon = icon

    def getModalidades(self):
        return ModalidadeEsporte.getByEsporte(self)
    
    def addPreferencia(self, player):
        EsportesPlayers(player, self)




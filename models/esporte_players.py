class EsportesPlayers:
    def __init__(self, player, esporte):
        self.player = player
        self.esporte = esporte

    def getEsportesPreferidos(self):
        return self.esporte.all().filter(player=self.player)

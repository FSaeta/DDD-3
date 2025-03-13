class EsportesPlayers:
    def __init__(self, player, esporte):
        self.player = player
        self.esporte = esporte

    def getByPlayer(self, player):
        return self.objects.all(player)
    
    def getByEsporte(self, esporte):
        return self.objects.all(esporte)

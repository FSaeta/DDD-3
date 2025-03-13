class Habilidade:
    def __init__(self, esporte, player, nivel, ultima_atualizacao):
        self.esporte = esporte
        self.player = player
        self.nivel = nivel
        self.ultimaAtualizacao = ultima_atualizacao

    def aumentarHabilidade(self):
        self.nivel += 1

    def abaixarHabilidade(self):
        self.nivel -= 1

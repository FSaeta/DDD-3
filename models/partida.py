from datetime import datetime


class Partida:
    name = ""
    player_ids = []

    owner_player_id = False
    local_id = False
    esporte_id = False

    data_hora = False
    valor_total = False
    max_jogadores = False


    def validateDate(self, data_hora):
        valid = True
        hora, minutos = data_hora.hour, data_hora.minute

        if hora <= self.local_id.horario_abre.hour:
            if hora == self.local_id.horario_abre.hour and minutos < self.local_id.horario_abre.minute:
                raise ValueError("Erro: O horário deve estar entre o horário de funcionamento do local.")


    def __init__(self, name, local, esporte, owner_player, data_hora, max_jogadores, valor, player_ids=[]):

        # Relational
        self.local_id = local
        self.esporte = esporte
        self.owner_player_id = owner_player_id
        self.addPlayer(owner_player_id)

        self.name = name
        self.data_hora = data_hora
        self.valor_total = valor
        self.max_jogadores = max_jogadores



    def addPlayer(self, player_id):
        if (self.getPlayersCount() + 1) > self.esporte_id.qu:
            raise ValueError("Erro: Partida cheia.")

        self.player_ids.append(player_id)
        return player_id

    def removePlayer(self, player_id):
        if player_id not in self.player_ids:
            raise ValueError("Erro: O jogador não está na partida.")
        self.player_ids.remove(player_id)
        return player_id

    def getPlayersCount(self):
        return len(self.player_ids or [])

    def getValorPorPessoa(self):
        return self.valor_total / self.max_jogadores

from players import PlayersAgg


class Partida:
    def __init__(self, name, local, modalidade_esporte, owner_player, data_hora, valor, players=[]):
        self.local = local
        self.owner_player = owner_player
        players.append(owner_player)
        self.players = PlayersAgg(self, modalidade_esporte, players)

        self.validateDate(data_hora)
        self.data_hora = data_hora

        self.name = name
        self.valor = valor

    def validateDate(self, data_hora):
        hora, minutos = data_hora.hour, data_hora.minute
        if hora <= self.local.horario_abre.hour:
            if hora == self.local_id.horario_abre.hour and minutos < self.local_id.horario_abre.minute:
                raise ValueError("Erro: O horário deve estar entre o horário de funcionamento do local.")
        return True

    def get_valor_por_pessoa(self):
        if self.players.getPlayersCount() == 0:
            return 0
        return self.valor_total / self.players.getMaxPlayers()

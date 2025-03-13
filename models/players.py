import requests
from esporte_players import EsportesPlayers
from habilidade import Habilidade



class User:
    def __init__(self, nome, username, email, senha, data_nascimento, endereco=None):
        self.nome = nome
        self.username = username
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Player(User):
    def __init__(self, nome, username, email, senha, data_nascimento):
        super(Player, self).__init__(nome, username, email, senha, data_nascimento)
        self.partidas = {}

    def getEsportes(self):
        return EsportesPlayers.getByPlayer(self)

    def addPartida(self, partida):
        partida.ownerPlayer = self
        self.partidas[partida] = partida
        return partida

    def getPartida(self, partida):
        return self.partidas.get(partida)

    def removePartida(self, partida):
        if partida.owner_player != self:
            raise ValueError("Somente o dono da partida pode excluí-la.")
        self.partidas.pop(self.getPartida())
    
    def getHabilidade(self, esporte):
        Habilidade.objects.filter(esporte=esporte, player=self)

class LocalManager(User):
    locais = {}

    def addLocal(self, local):
        if local.manager == self:
            self.locais[local] = local

    def inativarLocal(self, local):
        if local.manager == self:
            local.inativo = False

    def ativarLocal(self, local):
        if local.manager == self:
            local.inativo = True


class PlayersAgg:
    def __init__(self, partida, modalidade_esporte, players=[]):
        self.players = players
        self.partida = partida

        self.modalidadeEsporte = partida.esporte.getModalidades(
            ).get(modalidade_esporte)
        self.nivelHabilidade = partida.ownerPlayer.getHabilidade(
            self.modalidadeEsporte.esporte).nivel
        

    def addPlayer(self, player):
        if (self.getPlayersCount() + 1) > self.getMaxPlayers():
            raise ValueError("Erro: Partida cheia.")
        
        if player in self.players:
            raise ValueError("Erro: O jogador já está na partida.")

        self.players.append(player)
        return player
    
    def removePlayer(self, player):
        if player not in self.players:
            raise ValueError("Erro: O jogador não está na partida.")
        
        if player == self.partida.owner_player:
            raise ValueError("Erro: O dono da partida não pode sair da mesma.")

        self.players.remove(player)
        return player

    def getPlayers(self):
        return self.players

    def getPlayersCount(self):
        return len(self.getPlayers())
    
    def getMaxPlayers(self):
        return self.modalidadeEsporte.maxPlayers


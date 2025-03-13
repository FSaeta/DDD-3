class Local:

    def __init__(self, nome, endereco, img, esportes, manager):
        self.nome = nome
        self.endereco = endereco
        self.imagem = img
        self.esportes = esportes
        self.manager = manager

        self.ativo = True

    def toggleAtivo(self, manager, value=None):
        if manager == self.manager:
            if value is None:
                self.ativo = not(self.ativo)
            else:
                self.ativo = value


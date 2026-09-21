class No:
    def __init__(self,valor):
        self.dado = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)
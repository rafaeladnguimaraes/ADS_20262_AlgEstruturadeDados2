from no import No

class Arvore_b:
    def __init__(self):
        self.raiz = None
        self.total = 0
        self.diferentes = 0
        self.maior_freq = 0
        self.freq_palavra = ""

    def limpeza(self, palavra):
        palavra = palavra.lower()
        pontuacao = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        p_limpa = palavra.strip(pontuacao)
        return p_limpa
    
    def processar_texto(self, texto):
        palavras = texto.split()
        for p in palavras:
            palavra_l = self.limpeza(p)
        if palavra_l: 
            self.total += 1
            self.inserir(palavra_l)

    def inserir(self, palavra):
        if self.raiz is None:
            self.raiz = No(palavra)
            self.diferentes += 1
        else:
            self._i_rec(self.raiz, palavra)

    def _i_rec(self, no_atual, palavra):
        if palavra == no_atual.palavra:
            no_atual.freq += 1

        elif palavra < no_atual.palavra:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(palavra)
                self.diferentes += 1
            else:
                self._i_rec(no_atual.esquerda, palavra)

        else:
            if no_atual.direita is None:
                    no_atual.direita = No(palavra)
                    self.diferentes += 1
            else:
                self._i_rec(no_atual.direita, palavra)

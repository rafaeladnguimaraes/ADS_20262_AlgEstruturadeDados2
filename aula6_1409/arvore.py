from no import No

class Arvore:
    def __init__(self):
        self.raiz = None


    def inserir(self, no, pai = None):                
        if self.raiz is None:
            raiz = No(no)
        else:
            pai.adicionar_filho(no)
            

            
    def imprimirEmOrdem(self, raiz: No):
        if raiz is not None:
            while raiz.filhos:
                self.imprimirEmOrdem(raiz.filhos)
                print(raiz.dado, end = " - ")


    # def imprimirPreOrdem(self, raiz: No):
    #     if raiz is not None:
    #         print(raiz.dado, end = " - ")
    #         self.imprimirPreOrdem(raiz.esq)
    #         self.imprimirPreOrdem(raiz.dir)

    # def imprimirPosOrdem(self, raiz: No):
    #     if raiz is not None:
    #         self.imprimirPosOrdem(raiz.esq)
    #         self.imprimirPosOrdem(raiz.dir)
    #         print(raiz.dado, end = " - ")


    # def imprimirReverso(self, raiz: No):
    #     if raiz is not None:
    #         self.imprimirReverso(raiz.dir)
    #         print(raiz.dado, end = " - ") 
    #         self.imprimirReverso(raiz.esq)

    # def imprimirEmNivel(self, raiz: No):
    #     if raiz == None:
    #         return
    #     fila = Fila()
    #     fila.add( raiz )

    #     while fila.inicio != None:
    #         tamanho = fila.tamanho
    #         for _ in range( tamanho ):
    #             atual = fila.remover()
    #             print( atual.dado, end = " - ")

    #             if atual.esq != None:
    #                 fila.add( atual.esq )
    #             if atual.dir != None:
    #                 fila.add( atual.dir )

    #         print("")
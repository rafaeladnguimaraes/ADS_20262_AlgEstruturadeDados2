class Lista:
    def __init__(self):
        self.elemento = None
        self.inicio   = None
        self.fim      = None

    def vazio(self):
        if self.elemento is None:
            return True
        return False

    def adicionar(self, novo_elemento):
        if self.vazio():
            self.elemento = novo_elemento
            self.inicio   = novo_elemento
            self.fim      = novo_elemento
            return
        
        self.fim.prox = novo_elemento
        novo_elemento.ant = self.fim
        self.fim         = novo_elemento

    def insertion_sort(self):
        atual = self.inicio.prox

        while atual is not None:
            if atual > atual.prox:
                atual.ant = atual.prox
                if atual > atual.prox.prox:

        # for i in range(1, len(lista)):
        #     chave = lista[i]
        #     j = i - 1

        #     while j >= 0 and lista[j] > chave:
        #         lista[j + 1] = lista[j]
        #         j -= 1

        #     lista[j + 1] = chave

        # return lista


    # def ordena_insertion(self):
    #     if self.head is None or self.head.next is None:
    #         return

    #     atual = self.head.next
    #     while atual is not None:
    #         chave = atual.valor
    #         mover = atual.prev

    #         while mover is not None and mover.valor > chave:
    #             mover.next.valor = mover.valor
    #             mover = mover.prev

    #         if mover is None:
    #             self.head.valor = chave
    #         else:
    #             mover.next.valor = chave

    #         atual = atual.next
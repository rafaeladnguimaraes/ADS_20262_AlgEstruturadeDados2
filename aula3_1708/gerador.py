import random

class Gerar():
    def gerador():
        lista = [random.randint(1, 25) for i in range(20)]
        print (f"Lista: {lista}")
        return lista

lista = Gerar.gerador()


# Gerador de listas randomicas + Busca sequencial
import random

class Gerar:
    def gerador(qtd, final):
        contador = qtd
        lista = []
        num = 0
        while contador != 0:
            num = random.randint(0, final)
            lista.append(num)
            contador -= 1
        print (f"Lista: {lista}")
        return lista

# def busca(nume,lista):
#     for i, dado in enumerate(lista):
#         if dado == nume:
#             return i
#     return "Não encontrado"

# list = gerador(10, 25)
# result = busca(12, list)

# print(result)
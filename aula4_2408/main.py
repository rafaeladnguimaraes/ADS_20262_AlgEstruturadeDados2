from gerador_nums_inteiros import lista_de_inteiros
from aula4_2408.lista import Lista
from aula4_2408.nodo import Nodo


def adicionar_numeros_na_lista(minha_lista):
    for num in lista_de_inteiros:
        minha_lista.adicionar(Nodo(num))



lista_ED = Lista()
adicionar_numeros_na_lista(lista_ED)
lista_ED.print()

print("BUBBLE")
lista_ED.ordena_bubble()
print("SELECTION SORT")
lista_ED.ordena_selection()
lista_ED.print()

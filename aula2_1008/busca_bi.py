def busca_bi(valor, tam):
    lista = list(range(tam))
    ini = 0
    fim = tam
    while ini <= fim:
        meio = (ini + fim)//2
        print(f"Início: {ini}; meio: {meio}; fim: {fim}")
        if lista[meio] == valor:
            return f"Número encontrado, posição: {meio}"
        
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1

    return "Não encontrado, tente outro número"

busca = busca_bi(3,10)
print(busca)
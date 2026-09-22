import json

with open("sistema_arquivos.json", "r", encoding="utf-8") as arquivo_json:
    sistema_arquivos = json.load(arquivo_json)


def preOrdem(element, level=0):
    line = " " * level
    element_type = "FOLDER -" if element["tipo"] == "diretorio" else "FILE -"
    print(f"{line}{element_type}{element['nome']}")
    if element["tipo"] == "diretorio":
        for filho in element["filhos"]:
            preOrdem(filho, level + 1)

def posOrdem(element, level=0):
    if element["tipo"] == "diretorio":
            for filho in element["filhos"]:
                preOrdem(filho, level + 1)
    line = " " * level
    element_type = "FOLDER -" if element["tipo"] == "diretorio" else "FILE -"
    print(f"{line}{element_type}{element['nome']}")

def buscarElemento(element, search):
    

def alturaTotal():

def profundidade():

def folhasFinais():

def caminhoElemento():

def tamanhoTotal():

def buscarExtensao():

def estatisticasSistema():

def maiorDiretorio():
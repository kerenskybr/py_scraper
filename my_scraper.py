'''
Py_scraper

Web scraper usando beatiful soup

Destinado a captar dados de imóveis para treinar um algoritmo 
'''

from bs4 import BeautifulSoup
import requests
import os 
import os.path
import csv 
import time 
from urllib.request import urlopen 



def escreve_linha(linha, nome_arquivo):
    with open(nome_arquivo, 'a', encoding='utf-8') as grava:
        escreve = csv.writer(grava)
        escreve.writerows(linha)

def listagem(listagem):


    lista = []

    # prepare headers
    headers = {'User-Agent': 'Py_Scraper'}

    lista.append(['dorms', 'suite', 'vagas', 'bairro', 'area', 'valor' ])

    resposta = requests.get(listagem, headers=headers)

    scrap = BeautifulSoup(resposta.text, 'html.parser')


    for rows in scrap.find_all("section", class_="caracteristicas pull-left"):
        #if ("oddrow" in rows["class"]) or ("evenrow" in rows["class"]):    
        try:
            dorms = rows.find("li", class_="icone-quartos").get_text().replace(" quartos", "")
        except:
            dorms = 0
        try:
            suite = rows.find("li", class_="icone-suítes").get_text()
        except:
            suite = 0
        try:   
            vagas = rows.find("li", class_="icone-vagas").get_text(" ",strip=True)#.replace("vagas", "").replace("vaga", "")
        except:
            vagas = 0
        try:
            bairro = rows.find("span", class_="endereco pull-right").get_text(" ",strip=True).replace("\n", "")
        except:
            bairro = ""
        try:
            area = rows.find("li", class_="icone-area").get_text(" ",strip=True).replace("m", "").replace(" 2", "")
        except:
            area = 0
        try:
            valor = rows.find("div", class_="preco").get_text(" ",strip=True).replace("R$ ", "").replace("\n", "").replace(".", "").replace(",00", "").replace(" "" ", "")
        except:
            valor = 0

        lista.append([dorms, vagas, bairro, area, valor ])

    return lista


if __name__ == "__main__":

    nome_arquivo = "imoveis_capao.csv"

    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)

    site = 'https://www.zapimoveis.com.br/venda/casas/rs+capao-da-canoa/#{"precomaximo":"2147483647","parametrosautosuggest":[{"Bairro":"","Zona":"","Cidade":"CAPAO DA CANOA","Agrupamento":"","Estado":"RS"}],"pagina":"'

    pagina = 1

    resto = '","ordem":"Relevancia","paginaOrigem":"ResultadoBusca","semente":"82370447","formato":"Lista"}'

    #site = 'https://www.zapimoveis.com.br/venda/casas/rs+capao-da-canoa/'



   # resto = "2:%222%22,%22ordem%22:%22Relevancia%22,%22paginaOrigem%22:%22ResultadoBusca%22,%22semente%22:%22564095056%22,%22formato%22:%22Lista%22}"

    print("Inicializando...")
    while pagina < 19:
        listando = site + str(pagina) + resto
        listas = listagem(listando)

        escreve_linha(listas, nome_arquivo)
        pagina += 1

        print(".")

if pagina > 1:
    print("Scrap efetuado com sucesso! Gravando arquivo....")

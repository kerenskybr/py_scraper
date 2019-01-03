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

    resposta = requests.get(listagem)

    scrap = BeautifulSoup(resposta.text, 'html.parser')


    for rows in scrap.find_all("div"):
        #if ("oddrow" in rows["class"]) or ("evenrow" in rows["class"]):    
        try:
            dorms = rows.find("div", class_="destaque-caracteristicas-item destaque-dormitorios").get_text(" ",strip=True).replace("\n", "")
        except:
            dorms = 0
        try:   
            banhos = rows.find("div", class_="destaque-caracteristicas-item destaque-banheiros").get_text(" ",strip=True).replace("\n", "")
        except:
            banhos = 0
        try:
            bairro = rows.find("div", class_="destaque-bairro").get_text(" ",strip=True).replace("\n", "")
        except:
            bairro = ""
        try:
            area = rows.find("div", class_="destaque-caracteristicas-item destaque-area").get_text(" ",strip=True).replace(" m²", "").replace("\n", "")
        except:
            area = 0
        try:
            valor = rows.find("div", class_="destaque-valores").get_text(" ",strip=True).replace("Venda R$ ", "").replace("\n", "").replace(".", "").replace(",00", "").replace(" "" ", "")
        except:
            valor = 0

        lista.append([dorms, banhos, bairro, area, valor ])

    return lista


if __name__ == "__main__":

    nome_arquivo = "imoveis_osorio.csv"

    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)


    #site = 'http://itamarjardimimoveis.com.br/buscar?venda=Sim#ordem=bairro&amp;venda=Sim&amp;cidade[]=Osório'
    site = "http://itamarjardimimoveis.com.br/buscar?page="

    pagina = 1

    #resto = "&amp;venda=Sim"

    print("Inicializando...")
    while pagina < 16:
        listando = site + str(pagina)# + resto
        print(listando)
        listas = listagem(listando)

        escreve_linha(listas, nome_arquivo)
        pagina += 1

        print("_")

if pagina > 1:
    print("Scrap efetuado com sucesso! Gravando arquivo....")

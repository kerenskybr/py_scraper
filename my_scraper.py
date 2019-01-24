'''
Py_scraper

author : Roger Monteiro

Simple web scraper used to adquire data from house sales sites
You can change it to do anything you like to scrap
Remember to check robots.txt before scrap any data!
----
Simples web scraper para coletar dados de imóveis
Você pode adaptá-lo pro que quiser
Verifique sempre o arquivo robots.txt antes de usar um scraper!
'''

from bs4 import BeautifulSoup
import requests
import os 
import os.path
import csv 
import time 
from urllib.request import urlopen 

#Function to write line on csv file
#Função que escreve as linha no arquivo csv
def escreve_linha(linha, nome_arquivo):
    with open(nome_arquivo, 'a', encoding='utf-8') as grava:
        escreve = csv.writer(grava)
        escreve.writerows(linha)

#Function that scrap data
#Função que faz o scraping
def listagem(listagem):

    lista = []

    # prepare headers
    headers = {'User-Agent': 'Py_Scraper'}

    lista.append(['dorms', 'suite', 'vagas', 'bairro', 'area', 'valor' ])

    resposta = requests.get(listagem, headers=headers)

    scrap = BeautifulSoup(resposta.text, 'html.parser')

    # You have to look on your target site for the places with the data you want
    # Change 'section' and the name class

    # Você precisa manualmente procurar pelos valores no ste que quer usar o scraper
    # Procure por listas, divs, etc 
    for rows in scrap.find_all("section", class_="caracteristicas pull-left"):
        #if some exception occurs, the row receives 0
        #caso ocorra algum problema, o valor da linha é preenchido com um zero
        try:
            dorms = rows.find("li", class_="icone-quartos").get_text().replace(" quartos", "")
        except:
            dorms = 0
        try:
            suite = rows.find("li", class_="icone-suítes").get_text()
        except:
            suite = 0
        try:   
            vagas = rows.find("li", class_="icone-vagas").get_text(" ",strip=True)
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

    # Name of your csv file
    # Nome do seu arquivo csv
    nome_arquivo = "imoveis_capao.csv"

    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)

    # First goes the main page, number page, and 'resto' (if needed)
    # Para que o scraper va pulando as paginas, subistitua o numero da pagina pela variavel 'resto'

    site = 'https://www.zapimoveis.com.br/venda/casas/rs+capao-da-canoa/#{"precomaximo":"2147483647","parametrosautosuggest":[{"Bairro":"","Zona":"","Cidade":"CAPAO DA CANOA","Agrupamento":"","Estado":"RS"}],"pagina":"'

    pagina = 1

    resto = '","ordem":"Relevancia","paginaOrigem":"ResultadoBusca","semente":"82370447","formato":"Lista"}'

    print("Inicializando/Initializing...")
    while pagina < 19:
        listando = site + str(pagina) + resto
        listas = listagem(listando)

        escreve_linha(listas, nome_arquivo)
        pagina += 1

        print(".")

if pagina > 1:
    print("Scrap efetuado com sucesso! Gravando arquivo....")
    print("All done! Writing csv file....")

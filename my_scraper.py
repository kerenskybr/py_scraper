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


site = urlopen('http://itamarjardimimoveis.com.br/buscar?venda=Sim#ordem=bairro&amp;venda=Sim&amp;cidade[]=Osório')
scrap = BeautifulSoup(site.read(), 'html.parser')


dorms = scrap.find("div", class_="destaque-caracteristicas-item destaque-dormitorios").get_text(" ",strip=True).replace("\n", "")
banhos = scrap.find("div", class_="destaque-caracteristicas-item destaque-banheiros").get_text(" ",strip=True).replace("\n", "")
bairro = scrap.find("div", class_="destaque-bairro").get_text(" ",strip=True).replace("\n", "")
area = scrap.find("div", class_="destaque-caracteristicas-item destaque-area").get_text(" ",strip=True).replace(" m²", "").replace("\n", "")
valor = scrap.find("div", class_="destaque-valores").get_text(" ",strip=True).replace("Venda R$ ", "").replace("\n", "")

lista = []

lista.append([dorms, banhos, bairro, area, valor ])

print(lista)
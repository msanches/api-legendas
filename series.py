import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0"}

def scraping(categoria, page):
    data = []
    URL = "https://legendei.net/category/"+ categoria +"/page/" + str(page) + "/"
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("h3", class_="simple-grid-grid-post-title")

    for job_element in job_elements:
        title_element = job_element.find("a")
        link = title_element["href"].split("/")
        image = soup.find("img")
        temp = {'nome' : title_element.text.strip(), 
                #'link' : link[3],
                'link': '/legenda/' + link[3],
               'image' : image.get("src")
        }
        data.append(temp)
    return data

def buscar(nome, page):
    data = []
    URL = "https://legendei.net/page/"+page+"/?s="+ nome
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("h3", class_="simple-grid-grid-post-title")

    for job_element in job_elements:
        title_element = job_element.find("a")
        link = title_element["href"].split("/")
        image = soup.find('img')
        temp = {'nome' : title_element.text.strip(), 
                'link': '/legenda/' + link[3],
                'image' : image.get("src"),
                'qte_paginas': paginasBusca(nome)
        }
        data.append(temp)
    return data

def paginasBusca(nome):
    URL = "https://legendei.net/?s="+ nome
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    pages = int(soup.find("span", class_="sfwppa-pages").text.strip().split(" ")[3])
    return pages

def buscaLegenda(nome):
    #https://legendei.net/shazam-fury-of-the-gods-web-dl/
    data = []
    URL = "https://legendei.net/"+ nome
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("div", class_="entry-content simple-grid-clearfix")
    
    for div in job_elements:
        info = []
        link = div.find('a')['href']
        temp = div.find_all('p')
        for i in temp:
            info.append(i.text.strip())
        temp = {'download' : link, 'titulo' : info[0], 'Sinopse': info[3].split(":")[1].strip()}
        data.append(temp)
    return data
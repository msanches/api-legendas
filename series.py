import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0"}

def scraping(*args):
    data = []
    i = 0
    if not args:
        URL = "https://legendei.net/"
    else:
        categoria = args[0]
        page = args[1]
        URL = "https://legendei.net/category/"+ categoria +"/page/" + str(page) + "/"
    
    soup = util(URL)
    job_elements = soup.find_all("h3", class_="simple-grid-grid-post-title")
    images = soup.find_all("img") 

    for job_element in job_elements:
        title_element = job_element.find("a")
        link = title_element["href"].split("/")
        temp = {'nome' : title_element.text.strip(),
                'link': '/legenda/' + link[3],
                'image' : images[i].get("src")
        }
        i+=1
        data.append(temp)
    return data

def buscar(nome, page):
    data = []
    i = 0
    URL = "https://legendei.net/page/"+page+"/?s="+ nome

    soup = util(URL)
    job_elements = soup.find_all("h3", class_="simple-grid-grid-post-title")
    images = soup.find_all("img") 

    for job_element in job_elements:
        title_element = job_element.find("a")
        link = title_element["href"].split("/")
        temp = {'nome' : title_element.text.strip(), 
                'link': '/legenda/' + link[3],
                'image' : images[i].get("src"),
                'qte_paginas': paginasBusca(nome)
        }
        i+=1
        data.append(temp)
    return data

def paginasBusca(nome):
    URL = "https://legendei.net/?s="+ nome

    soup = util(URL)
    pages = int(soup.find("span", class_="sfwppa-pages").text.strip().split(" ")[3])
    return pages

def buscaLegenda(nome):
    #https://legendei.net/shazam-fury-of-the-gods-web-dl/
    data = []
    URL = "https://legendei.net/"+ nome
    soup = util(URL)
    
    job_elements = soup.find_all("div", class_="entry-content simple-grid-clearfix")
    
    for div in job_elements:
        info = []
        link = div.find('a')['href']
        temp = div.find_all('p')
        image = soup.find("img")
        for i in temp:
            info.append(i.text.strip())
        temp = {'download' : link, 
                'titulo' : info[0], 
                'sinopse': info[3].split(":")[1].strip(), 
                'imagem': image.get("src")
                }
        data.append(temp)
    return data

def util(url):
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    return soup
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
        link = title_element["href"].split('/')
        print(link[3])

def paginasBusca(nome):
    URL = "https://legendei.net/?s="+ nome
    #https://legendei.net/page/2/?s=bull
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    pages = int(soup.find("span", class_="sfwppa-pages").text.strip().split(" ")[3])
    print(pages)


def buscaLegenda(nome):
    #https://legendei.net/shazam-fury-of-the-gods-web-dl/
    data = []
    headers = {"User-Agent":"Mozilla/5.0"}
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
        temp = {'link' : link, 'info' : info}
        data.append(temp)
    return data
    

#print(buscaLegenda('shazam-fury-of-the-gods-web-dl'))
scraping('filmes', 1)

#https://legendei.net/page/2/?s=bull
#https://legendei.net/category/serie/
#https://legendei.net/category/filmes/
#URL = "https://legendei.net/page/" + str(i) + "/"
#https://legendei.net/?s=bull
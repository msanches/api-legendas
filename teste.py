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
    print('\n\n\n', data)

def util(url):
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    return soup


#print(buscaLegenda('shazam-fury-of-the-gods-web-dl'))
#scraping('filmes', 1)
scraping()

#https://legendei.net/page/2/?s=bull
#https://legendei.net/category/serie/
#https://legendei.net/category/filmes/
#URL = "https://legendei.net/page/" + str(i) + "/"
#https://legendei.net/?s=bull
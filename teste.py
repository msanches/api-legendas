import requests
from bs4 import BeautifulSoup

def scraping(categoria, page):
    data = []
    headers = {"User-Agent":"Mozilla/5.0"}
    URL = "https://legendei.net/category/"+ categoria +"/page/" + str(page) + "/"
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("h3", class_="simple-grid-grid-post-title")
    images = results.find_all('img')

    for job_element in job_elements:
        title_element = job_element.find("a")
        for image in images:

            temp = {'nome' : title_element.text.strip(), 
                    'link' : title_element["href"],
                    'image' : image.get("src")
            }
        data.append(temp)
        #print(title_element.text.strip(), " \t\t " ,title_element["href"])
    return data
def paginasBusca(nome):
    URL = "https://legendei.net/?s="+ nome
    #https://legendei.net/page/2/?s=bull
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    pages = int(soup.find("span", class_="sfwppa-pages").text.strip().split(" ")[3])
    print(pages)

paginasBusca('ncis')
print(scraping('serie', 1))

#https://legendei.net/page/2/?s=bull
#https://legendei.net/category/serie/
#https://legendei.net/category/filmes/
#URL = "https://legendei.net/page/" + str(i) + "/"
#https://legendei.net/?s=bull
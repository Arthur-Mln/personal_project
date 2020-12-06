import datetime
import sqlalchemy as db
from bs4 import BeautifulSoup
import requests

MAIN_URL = "https://www.vagas.com.br"
URL_CRAWL = input("Please enter the vagas.com.br URL to crawl :\n>> ")
URL_CRAWL = str(URL_CRAWL)

DATABASE_URL = "sqlite:///EmpregoBrasil.db"
engine = db.create_engine(DATABASE_URL, echo = True)
connection = engine.connect()
metadata = db.MetaData()
to_crawl_links = db.Table('JobOffers', metadata, autoload=True, autoload_with=engine)


req = requests.get(URL_CRAWL) #utiliser un headers ici éventuellement
soup = BeautifulSoup(req.text, "html.parser")

infos_header = soup.find_all("div", {"class": "informacoes-header"})
places = soup.find_all("span", {"class":{"vaga-local"}})
publications = soup.find_all("span", {"class":{"data-publicacao"}})


for info, place, publication in zip(infos_header, places, publications):

    end_link = info.find("a").get("href")
    link = MAIN_URL + end_link

    position = info.find("a").text.strip()
    company = info.find("span", {"class":"emprVaga"}).text.strip()
    level = info.find("span", {"class":"nivelVaga"}).text.strip()
    location = place.text.strip()
    released = publication.text

    ins = to_crawl_links.insert().values(url=link, position=position, company=company, level=level, place=location, publication_date=released, last_scrapped=datetime.datetime.now())
    connection.execute(ins)

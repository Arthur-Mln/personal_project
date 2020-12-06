## Brasil Jobs - Scrapping

The goal of this mini-project is :
* to create a SQL database after crawling a website.
* to deal with Sqlalchemy and BeautifulSoup
* to help a friend of mine in Brazil (Recife) !!

This is a opportunity to use the following Python librairies :

* BeautifulSoup : for web crawling (HTML)
* Sqlalchemy : manipulate/create sql tabs with python
* Requests : Web requests

We are going to crawl the following brazilian joboffers website :
https://www.vagas.com.br

First of all, you need to create a database.db in the same folder
Mine is called "EmpregoBrasil.db" (JobsBrazil)
To create the database, go to sqlite and enter (SQL command) :

CREATE TABLE JobOffers(
  url_id INTEGER PRIMARY KEY NOT NULL,
  url VARCHAR(150) NOT NULL UNIQUE,
  position VARCHAR(100) NOT NULL,
  company VARCHAR(100) NOT NULL,
  level VARCHAR(100) NOT NULL,
  place VARCHAR(100) NOT NULL,
  publication_date VARCHAR(50) NOT NULL,
  last_scrapped DATETIME DEFAULT NULL
  );

Once the script launched, it will ask you for a URL to crawl.
You just have to enter the "URL + City" you want to crawling as in the following instances.

EX : https://www.vagas.com.br/vagas-de-belo-horizonte
     https://www.vagas.com.br/vagas-de-recife
     https://www.vagas.com.br/vagas-de-rio-de-janeiro

Feel free to try it !

from bs4 import BeautifulSoup
import re
import urllib.request
from newspaper import Article
import datetime

currentPage = 0
idArticle = 1

while currentPage < 200:
    linkSearch = "https://www.dailymail.co.uk/home/search.html?offset=" + str(
        currentPage * 50) + "&size=50&type=article&days=all"
    page = urllib.request.urlopen(linkSearch)

    soup = BeautifulSoup(page, 'html.parser')

    strHtml = str(soup)
    arrayHref = re.findall('<h3 class=\"sch-res-title\">\s*<a href=\"(.*)\">.*<\/a>\s*<\/h3>', strHtml)

    for i in arrayHref:
        try:
            timeStartGetLink = datetime.datetime.now()
            linkArticle = 'https://www.dailymail.co.uk' + i
            article = Article(linkArticle, language='en')
            article.download()
            article.parse()
            articleContent = article.text
            timeEndGetLink = datetime.datetime.now()
            if (timeEndGetLink - timeStartGetLink).seconds > 5:
                print(1 / 0)
            fileNameArticle = str(idArticle) + '.txt'
            print(fileNameArticle)
            articleFile = open("file_articles/" + fileNameArticle, "w")
            articleFile.write(articleContent)
            articleFile.close()
            idArticle += 1
        except:
            print('Request Time Out !')

    currentPage += 1

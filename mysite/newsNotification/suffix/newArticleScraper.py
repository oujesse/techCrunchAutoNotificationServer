import bs4
import requests

# Gathers all of the urls of the latest articles on Techcrunch that the server has yet to see
def getTechcrunchArticleArray(oldFirst):
    res = requests.get('https://techcrunch.com/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    articleArr = []
    for i in range(len(soup.select('.post-block__title__link'))):
        if soup.select('.post-block__title__link')[i].get('href') == oldFirst: # ensures no seen articles are added
            break
        articleArr.append(soup.select('.post-block__title__link')[i].get('href'))
    return articleArr
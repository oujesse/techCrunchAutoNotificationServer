from .models import First, UserKeywords
from .suffix.newArticleScraper import getTechcrunchArticleArray
import bs4
import requests
from suffix_trees import STree
from webpush import send_user_notification

# Detects only new articles added to Techcrunch and notifies users that match these articles
def getNewTechcrunchArticles():
    # OldFirst represents the latest article already seen by the program
    if First.objects.first(): # Checks if there's currently a First object to avoid errors
        oldFirst = First.objects.first().firstUrl
    else:
        oldFirst = ''
    # Array of all new articles
    articleArr = getTechcrunchArticleArray(oldFirst)
    if len(articleArr) > 0:
        First.objects.all().delete()
        newFirst = First(firstUrl=articleArr[0])
        newFirst.save()
        for articleUrl in articleArr:
            st = STree.STree(bs4.BeautifulSoup(requests.get(articleUrl).text, 'lxml').select('.article-container')[0].text)
            for uk in UserKeywords.objects.all():
                # Checks if the any of the user's keywords match the article, notifies them if it does
                matching_words = []
                for word in uk.kw.words:
                    if st.find(word) != -1:
                        matching_words.append(word)
                if len(matching_words) > 0:
                    kw = uk.kw
                    kw.articles.append(articleUrl)
                    kw.matchedWords.append(matching_words)
                    kw.save()
                    payload = {"head": "Article Match Found Matching Keyword(s): " + str(matching_words), "body": articleUrl}
                    send_user_notification(user=uk.user, payload=payload, ttl=1000)

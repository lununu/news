import requests
import json
from newspaper import Article

def getNewsList(topic,fromDate,toDate):
# String,String,String --> List
# prints a list of dictionaries of the form:
# [{'author'      : 'newspublisher',
#   'description' : 'short text',
#   'newsText'    : 'long text',
#   'publishedAt' : 'yyyy-mm-ddThh:mm:ssZ',
#   'source'      : '{'id:None, 'name':'newspublisher' },
#   'title'       : '{'headline'},
#   'url'         : 'newspublisher.com/article',
#   'urlToImage'  : 'imgurl'},...]


      url = ('https://newsapi.org/v2/everything?'
             'q='+topic+'&'
             'from='+fromDate+'&'
             'to='+toDate+'&'
             'sortBy=publishedAt&'
             'apiKey=')
      response = requests.get(url).json()
      articleList = response['articles']

      for newsItem in articleList:
             currentArticle = Article(url=newsItem['url'], language='en', keep_article_html=True)     
             try:
                   currentArticle.download()
                   currentArticle.parse()
                   newsItem['newsText'] = currentArticle.text
             except:
                   pass
return articleList

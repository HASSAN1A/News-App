import urllib.request,json
from .models import Source
from .models import Article

# Getting news api key
api_key = None

# Getting the top headlines url
top_headlines_url = None
# Getting the sources url
sources_url = None
# Getting headlines by source name url
headlines_by_source_url= None
# Getting headlines by search name url
headlines_by_search_url= None
#Getting headlines by category name url
headlines_by_category_url= None


def configure_request(app):
    global api_key,top_headlines_url,sources_url,headlines_by_source_url,headlines_by_search_url,headlines_by_category_url 
    api_key = app.config['NEWS_API_KEY']
    top_headlines_url = app.config["NEWS_API_HEADLINES_URL"]
    sources_url = app.config["NEWS_API_SOURCES_URL"]
    headlines_by_source_url= app.config["NEWS_API_HEADLINES_BY_SOURCE_URL"]
    headlines_by_search_url=app.config["NEWS_API_HEADLINES_BY_SEARCH_URL"]
    headlines_by_category_url=app.config["NEWS_API_HEADLINES_BY_CATEGORY_URL"]

def get_sources():
    '''
    Function that gets the json response (i.e news sources) to our url request
    '''
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
            
    return sources_results



def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain source details

    Returns :
        sources_results: A list of source objects
    '''
    sources_results = []
    for source in sources_list:
      if source.get('id'):
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        
        source_object = Source(id,name,description)
        sources_results.append(source_object)

    return sources_results


def get_top_headlines():
    '''
    Function that gets the json response (i.e world top headlines news) to our url request
    '''
    get_headlines_url = top_headlines_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_articles(headlines_results_list)
            
    return headlines_results



def get_source_news(source_id):
    '''
    Function that gets the json response (i.e top headlines news by sources selected) to our url request
    '''
    get_source_news_url = headlines_by_source_url.format(source_id,api_key)

    with urllib.request.urlopen(get_source_news_url) as url:
        source_news_data = url.read()
        source_news_response = json.loads(source_news_data)

        source_news_results = None

        if source_news_response['articles']:
            source_news_list =source_news_response['articles']
            source_news_results = process_articles(source_news_list)
            
    return source_news_results


def get_category_news(category_name):
    '''
    Function that gets the json response (i.e top headlines news by category selected) to our url request
    '''
    get_category_news_url = headlines_by_category_url.format(category_name,api_key)

    with urllib.request.urlopen(get_category_news_url) as url:
        category_news_data = url.read()
        category_news_response = json.loads(category_news_data)

        category_news_results = None

        if category_news_response['articles']:
            category_news_list =category_news_response['articles']
            category_news_results = process_articles(category_news_list)
            
    return category_news_results

def search_news(article_name):
    '''
    Function that gets the json response (i.e top headlines news by article searched) to our url request
    '''
    search_news_url = headlines_by_search_url.format(article_name,api_key)

    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list =search_news_response['articles']
            search_news_results = process_articles(search_news_list)
            
    return search_news_results    




def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for article in articles_list:
      if article.get('urlToImage'):
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        article_img = article.get('urlToImage')
        published_at = article.get('publishedAt')
        content = article.get('content')

        article_object = Article(author,title,description,url,article_img,published_at,content)
        articles_results.append(article_object)

    return articles_results    


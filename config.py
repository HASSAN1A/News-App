import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_SOURCES_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_HEADLINES_BY_SOURCE_URL ='http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_HEADLINES_BY_SEARCH_URL='http://newsapi.org/v2/top-headlines?q={}&sortBy=publishedAt&apiKey={}'
    NEWS_API_HEADLINES_BY_CATEGORY_URL ='http://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

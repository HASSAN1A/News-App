from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_top_headlines,get_source_news,get_category_news,search_news

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources()
    top_headlines=get_top_headlines()[0:15]

    search_article = request.args.get('news_query')
    if search_article:
        return redirect(url_for('.search',news_article=search_article))
    else:    
        return render_template('index.html',sources = news_sources,headlines = top_headlines)


@main.route('/category/<category_name>')
def category_news(category_name):

    '''
    View category news page function that returns the category-news page and its data for the category selected
    '''
    articles=get_category_news(category_name)
    if articles:
        return render_template('category-news.html',category_name=category_name,articles=articles)
    else:
        return render_template('errors.html',error='article(s)')           


@main.route('/source/<source_id>')
def source_news(source_id):

    '''
    View source news page function that returns the source-news page and its data for the source selected
    '''
    source_articles=get_source_news(source_id)
    if source_articles:
        return render_template('source-news.html',articles=source_articles,source=source_id)        
    else:
        return render_template('errors.html',error='source articles')

@main.route('/search/<news_article>')
def search(news_article):
    '''
    View function to display the search results
    '''
    search_news_list = news_article.split(" ")
    search_news_format = "+".join(search_news_list)
    searched_news = search_news(search_news_format)
    title = f'search results for {news_article}'
    if searched_news:
        return render_template('search-news.html',title=title,articles = searched_news)    
    else:
        return render_template('errors.html',error='searched articles')    
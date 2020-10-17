class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,author,title,description,url,article_img,published_at,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.article_img = article_img
        self.published_at = published_at
        self.content = content
 


class Source:
  '''
  Source class to define Source Objects
  '''

  def __init__(self,id,name,description):
      self.id =id
      self.name = name
      self.description = description

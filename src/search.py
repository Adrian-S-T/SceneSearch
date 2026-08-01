from display import scene_printer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    search_words={stemmer.stem(word) for word in (keyword.lower()).split()}
    results=[]
    for element in scenes:
          name = {stemmer.stem(word) for word in element.anime.lower().split()}
          description = {stemmer.stem(word) for word in element.description.lower().split()}
          for word in search_words:
             if word in name:
                      score=score+3
             if word in description:
                      score=score+1
          if score>0:
             results.append((element,score))
    return results
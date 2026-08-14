from display import scene_printer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
from text_processing import process_text
def search_scenes(scenes,keyword):
    """searches for scenes in anime names and desc based on inputted keywords + counts matches"""
    search_words={stemmer.stem(word) for word in word_tokenize(keyword.lower())}
    results=[]
    for element in scenes:
          score=0 
          name = element.name_words
          description = element.description_words
          for word in search_words:
             score += 3 * name.count(word)
             score += description.count(word)
          if score>0:
             results.append((element,score))
    return results
def calculate_word_frequency(scenes):
   word_frequency={}
   for scene in scenes:
       words=set(scene.name_words+scene.description_words)
       for word in words:
         if word in word_frequency:
             word_frequency[word]+=1
         else:
             word_frequency[word]=1
   return word_frequency

